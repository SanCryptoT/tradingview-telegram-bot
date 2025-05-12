from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BOT_TOKEN = "7613972950:AAFqJ0iAlRxSY-rsPVUn3_G84KyhnSP1YVo"
CHAT_ID = "-1002287199347"

@app.route('/', methods=['GET'])
def home():
    return "Bot is running", 200

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Incoming data:", data)

    message = data.get('message', 'No message provided')
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    r = requests.post(url, json=payload)
    return jsonify(success=True), r.status_code
