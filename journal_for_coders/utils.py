from audioop import add
from datetime import datetime

import pymongo


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
    date, time = get_date_time()
    entry = {
        'date': date, 
        'time': time, 
        'title': title, 
        'entry': final_string
        }
    collection.insert_one(entry)

def get_all_entries(collection):
    cursor = collection.find({})
    l = []
    for document in cursor:
        print(document)
        print(type(document))
        l.append(document['entry'])
    return str(l[0])

_, _, collection = db_conn()
add_entry(collection, 'ipsum deleteFilesByType', 'rsdgrewdsfgr')

