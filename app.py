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
line_bot_api = LineBotApi('9nVCgPc4/2pt8oqecL9v/vyInP7cOWTMYwZT4AB//6hFi4bWXkS92287D4r2kTBONNogtObgJlgAhU9p5XW8ZCLYh/R7YVjFx6Jy+pLMisakzNAZnAfmJYT/lLcv0EJ3nh8X0VVKmg0gq+4zZMlKUwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('6cf6e13114e9f67a23e836fdecfab1c6')

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
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
