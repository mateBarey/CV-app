from flask import Flask, redirect, request

app = Flask(__name__)

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return redirect("https://cubas.dev/" + path, code=308)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)