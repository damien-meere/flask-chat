import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "randomstring"
messages = []

def add_messages(username, message):
    """Add messages to the `messages` list"""
    now = datetime.now().strftime("%H:%m:%S")
    messages_dict = {
        "timestamp":now,
        "from": username,
        "message": message
    }
    messages.append(messages_dict)
    #messages.append("({}) {}: {}".format(now, username, message))


@app.route("/", methods=["GET", "POST"])
def index():
    """Main page with instructions"""
    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(session["username"])

    return render_template("index.html")


@app.route("/<username>")
def user(username):
    """Display chat messages"""
    #return "<h1>Welcome, {0}</h1>{1}".format(username, messages)
    return render_template("chat.html", username = username, chat_messages = messages)

@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect back to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)


#app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)
#app.run(host="0.0.0.0", port=int(5000), debug=True)
app.run(host=os.environ.get('IP', "0.0.0.0"),
            port=int(os.environ.get('PORT', "5000")),
            debug=True)