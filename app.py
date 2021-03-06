#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

from flask import Flask, request

__author__ = 'enginebai'

#API_ROOT = 'api/'
#FB_WEBHOOK = 'fb_webhook'

app = Flask(__name__)


#
@app.route("/", methods=['GET'])
def receive_message_check():
    token_sent = request.args.get("hub.verify_token")
    #return verify_fb_token(token_sent)
    return "your app is succesfully deployed"

##We will receive messages that Facebook sends our bot at this endpoint


@app.route("/webhook", methods=['GET'])
def fb_webhook():
    verification_code = 'I_AM_VERIFICIATION_CODE'
    verify_token = request.args.get('hub.verify_token')
    if verification_code == verify_token:
        return request.args.get('hub.challenge')


#@app.route(API_ROOT + FB_WEBHOOK, methods=['POST'])
@app.route("/webhook", methods=['POST'])
def fb_receive_message():
    message_entries = json.loads(request.data.decode('utf8'))['entry']
    for entry in message_entries:
        for message in entry['messaging']:
            if message.get('message'):
                print("{sender[id]} says {message[text]}".format(**message))
    return "Hi"


if __name__ == '__main__':
    context = ('ssl/fullchain.pem', 'ssl/privkey.pem')
    app.run(host='0.0.0.0', debug=True, ssl_context=context)
