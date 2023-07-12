from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['get'])
def webhook():
    if request.method == 'GET':
        print("Data received from Webhook is: ", request.json)
        return "Webhook Server Up Running!"
    
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print("Data received from Webhook is: ", request.json)
        return "Webhook received!"

app.run(host='0.0.0.0', port=8088)