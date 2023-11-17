from flask import Flask, render_template, request
import string
import random

app = Flask(__name__)

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password(length):
    random.shuffle(characters)
    password = [random.choice(characters) for _ in range(length)]
    return "".join(password)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        length = int(request.form.get("password_length", 8))
        password = generate_password(length)
        return render_template("home.html", password=password)

    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
