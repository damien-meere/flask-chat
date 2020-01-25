import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "randomstring"
messages = []

def add_message(username, message):
    """Add messages to the `messages` list"""
    now = datetime.now().strftime("%H:%m:%S")
    messages.append({"timestamp":now, "from": username, "message": message})
    #messages.append("({}) {}: {}".format(now, username, message))


@app.route("/", methods=["GET", "POST"])
def index():
    """Main page with instructions"""
    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(url_for("user", username=session["username"]))

    return render_template("index.html")


@app.route("/chat/<username>", methods=["GET", "POST"])
def user(username):
    """Add and Display chat messages"""

    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_message(username, message)
        return redirect(url_for("user", username=session["username"]))
        #we use a redirect here rather than the standard render_template, as on refresh, all messages would be sent over and over again with the render_template

    #return "<h1>Welcome, {0}</h1>{1}".format(username, messages)
    return render_template("chat.html", username = username, chat_messages = messages)

#app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)
#app.run(host="0.0.0.0", port=int(5000), debug=True)
app.run(host=os.environ.get('IP', "0.0.0.0"),
            port=int(os.environ.get('PORT', "5000")),
            debug=True)