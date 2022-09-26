import datetime
from flask import Flask, render_template, request


app = Flask(__name__)

entries = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        entry_exemplo = request.form.get("exemplo")
        format_date = datetime.datetime.today().strftime("%d-%m-%y")
        entries.append((entry_exemplo, format_date))

    entries_with_date = [
        (
            entry[0],
            entry[1],
            datetime.datetime.strptime(entry[1], "%d-%m-%y").strftime("%b %d")
        )
        for entry in entries
    ]

    return render_template("index.html", entries=entries_with_date)


