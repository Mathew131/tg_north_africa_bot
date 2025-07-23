from flask import Flask, request
from flask_cors import CORS
from telegram import Bot
import asyncio
import os

app = Flask(__name__)
CORS(app)

TOKEN = "8081290799:AAEkWq-rSW4fBhg3VUm2_ePyJZipxltTF5g"
CHAT_ID = 1694842737

async def send_telegram(msg):
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=msg, parse_mode="HTML")

@app.route('/send', methods=['POST'])
def send():
    data = request.json
    print("Получено:", data)

    msg = "📩 <b>Новая заявка с сайта</b>\n\n"
    for key, value in data.items():
        msg += f"<b>{key}:</b> {value}\n"

    asyncio.run(send_telegram(msg))
    return {'status': 'ok'}

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)



