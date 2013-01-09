from config import host, port, resources
from flask import Flask, abort, request
from signature import verify_signature
from mdb import persist

app = Flask(__name__)

@app.route("/<resource>", methods=['POST'])
def serve(resource):
    found = filter(lambda x: x['name'] == resource, resources)
    if not found: 
        abort(404) 

    resource = found[0]
    if not request.args or not verify_signature(request.args.copy(), resource['secret']):
        abort(401)

    for k in request.form.iterkeys():
        persist(k, resource)

    return "OK"

if __name__ == "__main__":
    app.run(debug=True, host=host, port=port)
