import os
import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    client = MongoClient(os.environ.get("MONGODB_URI"))
    app.db = client.Microblog

    @app.route("/", methods=["GET", "POST"])
    def home():
        print([e for e in app.db.entries.find({})])
        if request.method == "POST":
            entry_exemplo = request.form.get("exemplo")
            format_date = datetime.datetime.today().strftime("%d-%m-%y")
            app.db.entries.insert_one({"exemplo": entry_exemplo, "date": format_date})

        entries_with_date = [
            (
                entry["exemplo"],
                entry["date"],
                datetime.datetime.strptime(entry["date"], "%d-%m-%y").strftime("%b %d")
            )
            for entry in app.db.entries.find({})
        ]

        return render_template("index.html", entries=entries_with_date)

    return app

