from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import back.neural_network.detection as detection


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/predict")
def predict():
    return Response(
        detection.camera_feed(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


# @app.route("/predict/data")
# def predict_data():
#     return jsonify(detection.prediction_data)


if __name__ == "__main__":
    app.run(debug=True)
