
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Flask Backend!",
        "status": "Running",
        "application": "Flask",
        "port": 5000
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/api/users")
def users():
    return jsonify({
        "users": [
            {"id": 1, "name": "Rahul"},
            {"id": 2, "name": "Priya"},
            {"id": 3, "name": "Amit"}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
