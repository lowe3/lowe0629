from django.conf import settings

from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def sendText(event1):
	try:
		message = TextSendMessage(
			text = "你的基礎代謝率為1024。"
		)
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
def sendQuickreply(event):
	try:
		message = TextSendMessage(
			text='請選擇您的運動頻率',
		quick_reply=QuickReply(
			items=[
				QuickReplyButton(
				action=MessageAction(label='久坐',text='久坐')
			),
				QuickReplyButton(
				action=MessageAction(label='除了通勤之外，不運動',text='除了通勤之外，不做其他運動')
			),  
				QuickReplyButton(
				action=MessageAction(label='每周有一兩天',text='每周有一兩天會做運動')
			), 
				QuickReplyButton(
				action=MessageAction(label='每周有三四天',text='每周有三四天會做運動')
			), 
				QuickReplyButton(
				action=MessageAction(label='每周有五六天',text='每周有五六天會做運動')
			), 
				QuickReplyButton(
				action=MessageAction(label='天天都運動',text='天天都會做運動')
				),
			]))
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))