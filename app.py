import os
from flask import Flask, request
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route('/webhook', methods=['GET','POST'])
def webhook():
    if request.method == 'POST':
        if request.headers.get('X-Hub-Signature') == os.environ.get('WEBHOOK_SECRET'):
            os.system(os.environ.get('WEBHOOK_SCRIPT'))
        return "Webhook received!"
    elif request.method == 'GET':
        return "Webhook Server is up and running!"

app.run(host='0.0.0.0', port=8088)