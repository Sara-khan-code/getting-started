from flask import Flask

app = Flask(__name__)

@app.route("/")

def func():
    return "Hello Sara"

if __name__ == "__main__":
    app.run(debug=True)