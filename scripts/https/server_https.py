from flask import Flask, url_for, request, jsonify
from flask_secure_headers.core import Secure_Headers
from functools import wraps
import json
import ssl
import socket
import os
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('cert4.pem', 'key4.pem')

if socket.gethostname() == "mssd-labs":
    os.chdir("/data/5/")

sh = Secure_Headers()
#sh.update({'HPKP':{'pins':[{'sha256':'uMBswu6zeZDgdpNzuimW9F1TLr66vBzdpuZgNXYyn/I='}],'max-age':2592000}})
#sh.update({'HSTS':{'max-age':2592000, 'includeSubDomains':True}})

app = Flask(__name__)

user=''

shadow={'admin':'l4sT_L4b', 'guest':'password'}

def check_auth(username, password):
    if username in shadow and shadow[username]==password:
        global user
        user=username
        return username
    else:
        return False

def authenticate():
    message = {'message': "Authenticate."}
    resp = jsonify(message)

    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Example"'

    return resp

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth: 
            return authenticate()
        user=check_auth(auth.username, auth.password)
        if not user:
            return authenticate()        
        return f(*args, **kwargs)

    return decorated

mdb={}

@app.route('/messages')
#@sh.wrapper()
@requires_auth
def api_messages():
    if user in mdb:
        return jsonify(messages=mdb[user])
    else:
        return jsonify(messages="")

@app.route('/message/<userid>', methods=['POST'])
@requires_auth
def api_message(userid):
    if not userid in mdb:
        mdb[userid]=[]
    mdb[userid].append("From %s: %s"%(user,request.json['message']))
    print ("Message received from user %s for user %s: %s"%(userid,user,request.json['message']))
    return "Thank you for your message\n"

if __name__ == '__main__':
    #context = ('cert.pem', 'key.pem')
    app.run(host='0.0.0.0', port=443, ssl_context=context, threaded=True, debug=True)
