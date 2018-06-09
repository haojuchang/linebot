from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('kt6IJ/UnjF9vKp3YLpceIGPn5gPzPismP46p0Uk2qM0uONry/QRMPrIQj+ACwuFjGr1tMJ9+NBBHvPZOuJXQUAl8HAYs9q78JH03aqx5JatG+r59K7jC2CUAh/+Slyy7PVdvHlv/HI60dUmazQsajwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('e28040c3dd87d1c2623177ead74596d2')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	temp = ["寶貝你最漂亮了", "you are so beautiful", "妳是天使", "你的腿兒好修長呀", "來來來~我帶妳出去玩", "我不會再睡啦><", "想你抱抱呀", "你最可愛了", "我愛妳呀"]
    message = TextSendMessage(text="FOSS 說: %s" % temp[1])
    line_bot_api.reply_message(
        event.reply_token,
        message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
