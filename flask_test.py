from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "HOME OK"

@app.route("/test")
def test():
    return "TEST OK"

if __name__ == "__main__":
    app.run(debug=True)
