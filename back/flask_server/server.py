from flask import Flask, request, jsonify, Response
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import back.neural_network.detection as detection


app = Flask(__name__)


@app.route("/predict")
def predict():
    return Response(
        detection.camera_feed(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


if __name__ == "__main__":
    app.run(debug=True)
