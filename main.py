import flask
import manager

app = flask.Flask(__name__)
opts = manager.load_json("flask")
payload = manager.load_json("resources")

@app.route("/", methods=["GET"])
def index():
    ctx = {
        "data": payload["master"],
        "titles": list(payload["master"].keys()),
        "cgen": manager.cgen
    }

    return flask.render_template("index.html", **ctx)

@app.route("/api/master", methods=["GET"])
def api_master():
    return flask.jsonify(payload)

app.run(**opts)
