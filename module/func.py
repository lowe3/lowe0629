from django.conf import settings

from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def sendText(event1):
	try:
		message = TextSendMessage(
			text = "你的基礎代謝率為1024，請回傳好。"
		)
		line_bot_api.reply_message(event1.reply_token,message)
	except:
		line_bot_api.reply_message(event1.reply_token,TextSendMessage(text='發生錯誤!'))
def sendQuickreply(event):
	try:
		message = TextSendMessage(
		text='請選擇您的運動頻率',
		quick_reply=QuickReply(
			items=[
				QuickReplyButton(
				action=MessageAction(label="久坐",text="久坐")
			),  
				QuickReplyButton(
				action=MessageAction(label="每周有輕鬆的運動3-5天",text="每周有輕鬆的運動3-5天")
			), 
				QuickReplyButton(
				action=MessageAction(label="每周有中等強度的運動3-5天",text="每周有中等強度的運動3-5天")
			), 
				QuickReplyButton(
				action=MessageAction(label="每周有高強度的運動6-7天",text="每周有高強度的運動6-7天")
			), 
				QuickReplyButton(
				action=MessageAction(label="勞力密集的工作或每天訓練",text="勞力密集的工作或每天訓練甚至一天訓練兩次")
				),
			]))
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
	
