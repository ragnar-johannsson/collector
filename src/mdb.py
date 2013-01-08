from json import loads as jsonify
from pymongo import MongoClient

def persist(data, config):
    conn = MongoClient(config['mongodb_host'], config['mongodb_port'])
    db = conn[config['mongodb_db']]
    collection = db[config['mongodb_collection']]

    collection.insert(jsonify(data))
