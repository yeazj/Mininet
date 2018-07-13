from flask import Flask, url_for, request, jsonify, redirect, flash, render_template, request, session, abort
from flask_secure_headers.core import Secure_Headers
#from flask_sslify import SSLify
from functools import wraps
import json
import ssl
import socket
import os
import ssl
from sqlalchemy.orm import sessionmaker
from createtable import *

engine = create_engine('postgresql://postgres:postgres@10.0.2.15:5432/test', echo=True)

#context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
#context.load_cert_chain('cert3.pem', 'key3.pem')

if socket.gethostname() == "mssd-labs":
    os.chdir("/data/5/")

sh = Secure_Headers()

app = Flask(__name__)
#sslify = SSLify(app)

thisuser=''

#shadow={'admin':'l4sT_L4b', 'guest':'password'}

def check_auth(usernm, passwd):
    #if username in shadow and shadow[username]==password:
    #    global thisuser
    #    thisuser=username
    #    return username
    #else:
    #    return False

    Session = sessionmaker(bind=engine)
    s = Session()
    #query = s.query(User).filter(User.username.in_(usernm), User.password.in_(passwd) )
    query = s.query(User).filter(User.username.in_(usernm), User.password.in_(passwd) )
    result = query.first()
    print "Result :", result
    if result:
        global thisuser
        thisuser=usernm
        return usernm
    else:
        flash('wrong password!')
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
        thisuser=check_auth(auth.username, auth.password)
        if not thisuser:
            return authenticate()        
        return f(*args, **kwargs)

    return decorated


mdb={}
@app.route('/messages')
@requires_auth
def api_messages():
    if thisuser in mdb:
        return jsonify(messages=mdb[thisuser])
    else:
        return jsonify(messages="")

@app.route('/message/<userid>', methods=['POST'])
@requires_auth
def api_message(userid):
    if not userid in mdb:
        mdb[userid]=[]
    mdb[userid].append("From %s: %s"%(thisuser,request.json['message']))
    print ("Message received from user %s for user %s: %s"%(userid,thisuser,request.json['message']))
    return "Thank you for your message\n"

if __name__ == '__main__':
    #context = ('cert.pem', 'key.pem')
    #app.run(host='0.0.0.0', port=80, ssl_context=context, debug=True) #threaded=True, 
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=80, debug=True) #threaded=True, ssl_context=context
