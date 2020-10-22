from django.conf import settings

from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction, ButtonsTemplate, URITemplateAction, ConfirmTemplate, PostbackTemplateAction, TemplateSendMessage
import random
from funclapi.models import users, seven, wefamily, user

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def sendText(event):
	try:
		message = TextSendMessage(
			text = "你的基礎代謝率為1024，請回傳好。"
		)
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
def sendImage(event):
	try:
		message = ImageSendMessage(
			original_content_url = "https://imgur.com/eIejLVQ.jpg",preview_image_url = "https://imgur.com/eIejLVQ.jpg"
		)
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
def sendQuickreply(event):
	try:
		message = TextSendMessage(
		text='請選擇超商',
		quick_reply=QuickReply(
			items=[
				QuickReplyButton(
				action=MessageAction(label="7-11",text="@7-11")
			),  
				QuickReplyButton(
				action=MessageAction(label="全家",text="@全家")
			), 
			]))
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
		
def sendQuickreply(7-11):
	try:
		message = TextSendMessage(
		text='請選擇您目前是哪一餐',
		quick_reply=QuickReply(
			items=[
				QuickReplyButton(
				action=MessageAction(label="早餐",text="@早餐")
			),  
				QuickReplyButton(
				action=MessageAction(label="午餐",text="@午餐")
			), 
				QuickReplyButton(
				action=MessageAction(label="晚餐",text="@晚餐")
			),
			]))
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))

# def sendQuickreply(event2):
	# try:
		# message = TextSendMessage(
		# text='請選擇您目前是哪一餐',
		# quick_reply=QuickReply(
			# items=[
				# QuickReplyButton(
				# action=MessageAction(label="早餐",text="@早餐")
			# ),  
				# QuickReplyButton(
				# action=MessageAction(label="午餐",text="@午餐")
			# ), 
				# QuickReplyButton(
				# action=MessageAction(label="晚餐",text="@晚餐")
			# ),
			# ]))
		# line_bot_api.reply_message(event.reply_token,message)
	# except:
		# line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
# def sendchoise(event):
	# try:
		# message = TemplateSendMessage(
			# alt_text="確認超商",
			# template=ConfirmTemplate(
				# text="請選擇你購買食品的超商",
				# actions=[
					# MessageTemplateAction(
						# label="7-11",
						# data="7-11"
					# ),
					# MessageTemplateAction(
						# label="全家"
						# data="全家"
					# )
				# ]
			# )
		# )	
		# line_bot_api.reply_message(event.reply_token,message)
	# except:
		# line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))	