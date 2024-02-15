from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def indexx():
    return render_template("index.html")

#Localhost http://127.0.0.1:5000/name
@app.route("/user/<name>")

def user(name):
    
    return f"<h1>hello there!! {name}</h1>"


if __name__ == "__main__":
    app.run(debug =True)