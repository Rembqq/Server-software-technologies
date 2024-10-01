from webapp import app
from flask import jsonify
from datetime import datetime


@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    response = {
        "status": "Service is running",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return jsonify(response), 200
