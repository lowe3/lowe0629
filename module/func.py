from django.conf import settings

from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction, ButtonsTemplate, URITemplateAction, ConfirmTemplate, PostbackTemplateAction, TemplateSendMessage
import random
from funclapi.models import users, seven, wefamily, user, food

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
		datetimee = datetime.datetime.strptime(str_p,'%Y-%m-%d %H:%M')
		date_time = datetimee.strftime("%m-%d-%Y, %H:%M")
		eitems = flist[3]
		# user_id = event.source.user_id
		# if food.objects.filter(items=flist[3]).exists() and user.objects.filter(uid=user_id).exists():
			# for fitems in food.objects.filter(items=flist[3]):
				# ecalories = fitems.calories
			# for fuser in user.objects.filter(uid=user_id)
				# ebmr = fuser.bmr
				# etdee = fuser.tdee
		# unit = eat.objects.create(uid=user_id, bmr=ebmr, tdee=etdee, date=edate, time=etime, items=eitems, calories=ecalories)  #寫入資料庫
		# unit.save()
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text='您的餐點紀錄已成功輸入，輸入內容如下:'+'\n日期時間：'+edatetime+'\n產品名稱：'+eitems))
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
