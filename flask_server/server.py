from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route("/predict")
def predict():
    return {"message": ["Hello, World!", "Hello, World!"]}

if __name__ == "__main__":
    app.run(debug=True)