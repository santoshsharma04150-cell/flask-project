from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <img src="/static/jiren.jpg"width="300" height="500">
    <img src="/static/image.png" width="500" height="1000">
    """

if __name__ == "__main__":
    app.run(debug=True)