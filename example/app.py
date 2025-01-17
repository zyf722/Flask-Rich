from flask import Flask

from flask_rich import RichApplication

app = Flask(__name__)
rich = RichApplication(app)

app.logger.setLevel("DEBUG")


@app.route("/")
def index():
    app.logger.debug("If this is [red]colorful[/red], everything worked!")
    app.logger.debug("1, 2.4, True, False, None")
    return "INDEX"


@app.route("/error")
def error():
    raise Exception
    return "error"


@app.route("/test/<string:x>", methods=["GET", "POST"])
def test(x: str):
    return x


if __name__ == "__main__":
    app.run()
