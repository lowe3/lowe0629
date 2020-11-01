from django.conf import settings

from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction, ButtonsTemplate, URITemplateAction, ConfirmTemplate, PostbackTemplateAction, TemplateSendMessage
import random
from funclapi.models import users, seven, wefamily, user, food, eat

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
# def sendQuickreply(event):
	# try:
		# message = TextSendMessage(
		# text='請選擇超商',
		# quick_reply=QuickReply(
			# items=[
				# QuickReplyButton(
				# action=MessageAction(label="7-11",text="@7-11")
			# ),  
				# QuickReplyButton(
				# action=MessageAction(label="全家",text="@全家")
			# ), 
			# ]))
		# line_bot_api.reply_message(event.reply_token,message)
	# except:
		# line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))

def sendQuickreply(event):
	try:
		message = TextSendMessage(
		text='請選擇種類',
		quick_reply=QuickReply(
			items=[
				QuickReplyButton(
				action=MessageAction(label="飯類",text="飯類")
			),  
				QuickReplyButton(
				action=MessageAction(label="麵類",text="麵類")
			), 
				QuickReplyButton(
				action=MessageAction(label="麵包",text="麵包")
			),  
				QuickReplyButton(
				action=MessageAction(label="甜點",text="甜點")
			),
				QuickReplyButton(
				action=MessageAction(label="沙拉",text="沙拉")
			),  
				QuickReplyButton(
				action=MessageAction(label="關東煮",text="關東煮")
			),
				QuickReplyButton(
				action=MessageAction(label="湯類",text="湯類")
			),  
				QuickReplyButton(
				action=MessageAction(label="水果",text="水果")
			),
				QuickReplyButton(
				action=MessageAction(label="飲料",text="飲料")
			),  
				QuickReplyButton(
				action=MessageAction(label="其他",text="其他")
			),	
				QuickReplyButton(
				action=MessageAction(label="醬料",text="醬料")
			),			
			]))
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))

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