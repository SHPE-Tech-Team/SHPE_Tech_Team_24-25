from flask import Flask, request, jsonify, Response,current_app
from flask_cors import CORS
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import back.neural_network.detection as detection


app = Flask(__name__)
CORS(
    app,
    resources={
        r"/*": {
            "origins": ["http://localhost:3000"],
            "methods": ["GET", "POST", "OPTIONS"],
            "allow_headers": ["Content-Type"],
        }
    },
)

# prediction_data = {
#     "data": {
#         "confidence": 0.0,
#         "class": "none",
#         "predicted_idx": -1,
#     }
# }


@app.route("/predict")
def predict():
    return Response(
        detection.camera_feed(True),
        mimetype="multipart/x-mixed-replace; boundary=frame",
        headers={
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0",
            "Access-Control-Allow-Origin": "http://localhost:3000",
        },
    )


# @app.route("/data")
# def fetch_data():
# return jsonify(prediction_data)


@app.route("/data")
def fetch_data():
    if hasattr(current_app, "prediction_data"):
        return jsonify(current_app.prediction_data)
    else:
        return jsonify(
            {"data": {"confidence": 0.0, "class": "none", "predicted_idx": -1}}
        )


@app.route("/update_prediction", methods=["POST", "GET"])
def update_prediction():
    if request.method == "POST":
        try:
            data = request.json
            app.logger.info(f"Received POST data: {data}")

            # Store the updated data in the application context
            if not hasattr(current_app, "prediction_data"):
                current_app.prediction_data = {"data": {}}
            current_app.prediction_data["data"].update(data)

            return jsonify({"status": "success"})
        except Exception as e:
            app.logger.error(f"Error processing POST request: {e}")
            return jsonify({"status": "error", "message": str(e)}), 400
    else:
        # Handle GET request - return current prediction data
        app.logger.info("Received GET request to update_prediction")
        if hasattr(current_app, "prediction_data"):
            return jsonify(current_app.prediction_data)
        else:
            return jsonify({"data": {}})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
