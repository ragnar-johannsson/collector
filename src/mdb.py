import logging

from json import loads as jsonify
from pymongo import MongoClient

connections = dict()

def initdb(resources):
    for config in resources:
        if 'mongodb_user' in config:
            url = 'mongodb://%s:%s@%s' % (config['mongodb_user'], config['mongodb_passwd'], config['mongodb_host'])
        else:
            url = 'mongodb://%s' % config['mongodb_host']
        if 'mongodb_port' in config:
            url += ":%s" % config['mongodb_port']

        logging.debug('Connecting to %s' % url)
        connections[config['name']] = MongoClient(url, max_pool_size=20)

def persist(data, config):
    db = connections[config['name']][config['mongodb_db']]
    collection = db[config['mongodb_collection']]

    collection.insert(jsonify(data))
