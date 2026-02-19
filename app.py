from flask import Flask, jsonify
from services import calculate_customer_score
from utils.logger import log_info

app = Flask(__name__)

@app.route("/")
def home():
    log_info("Home endpoint accessed")
    return "Customer Analytics API Running"

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/score")
def score():
    result = calculate_customer_score()
    return jsonify({"customer_score": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
