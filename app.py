from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="./build")


@app.route("/banner")
def banner():
    return "welcome!"


@app.route("/")
def index():
    return send_from_directory('./build', "index.html")


@app.route("/<path:path>")
def base(path):
    return send_from_directory('./build', path)


if __name__ == "__main__":
    app.run()
