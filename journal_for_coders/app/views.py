from datetime import datetime

import pymongo
from flask import render_template

from app import app

# from utils import *

class utils():
    def db_conn():
        client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.8gzim.mongodb.net/coderJournal?retryWrites=true&w=majority")
        db = client.get_database('coderJournal')
        collection = db.entries
        return client, db, collection
        # print(entries.count_documents({}))

    def get_date_time():
        now = datetime.now()
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M") 
        return date, time

    def parse_entry_String():
        # parse txt or whatever file is needed into basic string with '\n\ for new lines
        pass

    def add_entry(collection, title, final_string):
        date, time = utils.get_date_time()
        entry = {
            'date': date, 
            'time': time, 
            'title': title, 
            'entry': final_string
            }
        collection.insert_one(entry)

    def get_all_entries(collection):
        cursor = collection.find({})
        dates = []
        times = []
        titles = []
        entries = []
        for document in cursor:
            print(document)
            print(type(document))
            dates.append(document['date'])
            times.append(document['time'])
            titles.append(document['title'])
            entries.append(document['entry'])
        return dates, times, titles, entries



@app.route("/")
def index():
    client, db, collection = utils.db_conn()
    dates, times, titles, entries = utils.get_all_entries(collection)
    return render_template("public/index.html", length = int(len(dates)), dates = dates, times = times, titles = titles, entries = entries)

@app.route("/about")
def about():
    return """
    <h1 style='color: red;'>I'm a red H1 heading!</h1>
    <p>This is a lovely little paragraph</p>
    <code>Flask is <em>awesome</em></code>
    """
