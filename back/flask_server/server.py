from flask import Flask, request, jsonify, Response, current_app
from flask_cors import CORS
import sys
from flask_socketio import SocketIO, emit
import socketio
import threading
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
# import back.neural_network.detection as detection
from back.neural_network import detection


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

prediction_data = {
    "data": {
        "confidence": 0.0,
        "class": "none",
        "predicted_idx": -1,
    }
}
socketio = SocketIO(app, cors_allowed_origins="http://localhost:3000")


# @socketio.on("/predict")
@app.route("/predict")
def predict():
    return Response(
        detection.camera_feed(),
        mimetype="multipart/x-mixed-replace; boundary=frame",
        headers={
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0",
            "Access-Control-Allow-Origin": "http://localhost:3000",
        },
    )


@app.route("/data")
def fetch_data():
    return jsonify(prediction_data)


@socketio.on("connect")
def handle_connect():
    print("Client connected")
    socketio.send("Connected")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
    # socketio.run(app, debug=True, host="0.0.0.0", port=8080)
