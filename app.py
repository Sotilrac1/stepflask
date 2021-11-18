from flask import Flask, render_template, redirect, session, url_for,request

app = Flask(__name__)
app.secret_key = "hello"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        return render_template("index.html")
    
@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]     
        return f"<h1>{user}</h1>"
    else:
        return redirect("index.html")
if __name__ == "__main__":
    app.run(debug=True)