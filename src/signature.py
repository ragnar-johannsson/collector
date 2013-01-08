import hmac
from base64 import urlsafe_b64encode as b64encode
from hashlib import sha1
from time import time

def verify_signature(params, key):
    if 'signature' not in params or 'timestamp' not in params:
        return False

    remote_time = int(params.get('timestamp'))
    local_time = int(time())

    if not (local_time-600 < remote_time < local_time+600):
        return False

    remote_signature = params.get('signature')
    del params['signature']
    query = '&'.join('%s=%s' % (k, params[k]) for k in sorted(params.iterkeys())) 
    local_signature = b64encode(hmac.new(key, query, sha1).digest())

    if remote_signature == local_signature:
        return True
