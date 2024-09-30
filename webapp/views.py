from webapp import app


@app.route("/healthcheck")
def hello_world():
    return "OK", 200