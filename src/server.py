import logging

from config import host, port, resources
from flask import Flask, abort, request
from mdb import persist, initdb
from signature import verify_signature

app = Flask(__name__)

@app.route("/<resource>", methods=['POST'])
def serve(resource):
    logging.debug('Connection from: %s' % request.remote_addr)
    logging.debug('Resource: %s' % resource)
    logging.debug('Query string %s' % request.query_string)

    found = filter(lambda x: x['name'] == resource, resources)
    if not found: 
        abort(404) 

    resource = found[0]
    if not request.args or not verify_signature(request.args.copy(), resource['secret']):
        abort(401)

    try:
        for k in request.form.iterkeys():
            logging.debug('Request data: %s' % k)
            persist(k, resource)
    except Exception as e:
        logging.error('Error persisting data: %s' % str(e))
        return "Error saving data", 500

    return "OK"

if __name__ == "__main__":
    initdb(resources)
    app.run(debug=True, host=host, port=port)
