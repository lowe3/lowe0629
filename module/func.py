from django.conf import settings
import datetime
from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction, ButtonsTemplate, URITemplateAction, ConfirmTemplate, PostbackTemplateAction, TemplateSendMessage
import random
from funclapi.models import users, seven, wefamily, user, food, eat

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def sendImage(event):
	try:
		message = ImageSendMessage(
			original_content_url = "https://imgur.com/eIejLVQ.jpg",preview_image_url = "https://imgur.com/eIejLVQ.jpg"
		)
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
	
def manageForm(event, mtext, user_id):
	try:
		flist = mtext[3:].split()
		edatetime = flist[0]		#取得輸入資料
		# edt = ''.join([x for x in edatetime if x.isdigit()])     #抓取數字
		datetimee = datetime.strptime(edatetime, '%Y-%m-%d-%H:%M')
		# date_time = datetime.strftime(datetimee, "%m-%d-%Y, %H:%M")
		eitems = flist[3]
		# user_id = event.source.user_id
		# if food.objects.filter(items=eitems).exists():
		for fitems in food.objects.filter(items=eitems):
			content='\n熱量:'+fitems.calories
			# for fuser in user.objects.get(uid=user_id):
			unit = eat.objects.create(uid=user_id, bmr=user.objects.get(uid=user_id).bmr, tdee=user.objects.get(uid=user_id).tdee, datetime=datetimee, items=eitems, calories=fitems.calories)  #寫入資料庫
			unit.save()
			line_bot_api.reply_message(event.reply_token, TextSendMessage(text='您的餐點紀錄已成功輸入，輸入內容如下:'+'\n日期時間：'+edatetime+'\n產品名稱：'+eitems+content))
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
