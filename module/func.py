from django.conf import settings
import datetime
from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction, ButtonsTemplate, URITemplateAction, ConfirmTemplate, PostbackTemplateAction, TemplateSendMessage
import random
from funclapi.models import wefamily, user, food, eat
from linebot.models import *
from datetime import datetime, timedelta
from linebot.models import MessageEvent, TextSendMessage, TextMessage


line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def sendImage(event):
	try:
		message = ImageSendMessage(
			original_content_url = "https://imgur.com/eIejLVQ.jpg",preview_image_url = "https://imgur.com/eIejLVQ.jpg"
		)
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
		
def sendQuickreply(event, user_id):  #快速選單
    try:
		dt = datetime.now().strftime('%Y-%m-%d')
		if eat.objects.filter(uid=user_id, datetime=dt).exists():
			content = '您今日已攝取熱量為:' + eat.objects.filter(uid=user_id, datetime=dt).last().total + '大卡' + '\n請選擇您現在想吃的食物種類'
		else:
			content = '您今日尚未攝取熱量。' + '\n請選擇您現在想吃的食物種類'
		message = TextSendMessage(
			text=content,
			quick_reply=QuickReply(
				items=[
					QuickReplyButton(
						action=MessageAction(label="飯類", text="飯類")
					),
					QuickReplyButton(
						action=MessageAction(label="麵類", text="麵類")
					),
					QuickReplyButton(
						action=MessageAction(label="沙拉", text="沙拉")
					),
					QuickReplyButton(
						action=MessageAction(label="麵包", text="麵包")
					),
					QuickReplyButton(
						action=MessageAction(label="飲料", text="飲料")
					),
					QuickReplyButton(
						action=MessageAction(label="關東煮", text="關東煮")
					),
					QuickReplyButton(
						action=MessageAction(label="甜點", text="甜點")
					),
					QuickReplyButton(
						action=MessageAction(label="湯類", text="湯類")
					),	
					QuickReplyButton(
						action=MessageAction(label="水果", text="水果")
					),
					QuickReplyButton(
						action=MessageAction(label="其他", text="其他")
					),					
				]
			)
		)
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
	
def manageForm(event, mtext, user_id):
	try:
		flist = mtext[3:].split()
		edate = flist[0]
		etime = flist[1]#取得輸入資料
		estore = flist[2]
		eitems = flist[4]
		for fitems in food.objects.filter(items=eitems, convenience=estore):
			content='\n熱量:'+str(fitems.calories)+'大卡'
			if not (eat.objects.filter(uid=user_id, datetime=edate).exists()):
				unit = eat.objects.create(uid=user_id, bmr=user.objects.get(uid=user_id).bmr, tdee=user.objects.get(uid=user_id).tdee, datetime=edate, items=eitems, calories=fitems.calories, total=fitems.calories, times=1)  #寫入資料庫
				unit.save()
				line_bot_api.reply_message(event.reply_token, TextSendMessage(text='您的餐點紀錄已成功輸入，輸入內容如下:'+'\n日期:'+edate+'\n時間：'+etime+'\n產品名稱：'+eitems +content))
			else:
				etotal = eat.objects.filter(uid=user_id, datetime=edate).last().total + food.objects.get(items=eitems, convenience=estore).calories
				etimes = eat.objects.filter(uid=user_id, datetime=edate).last().times + 1
				unit = eat.objects.create(uid=user_id, bmr=user.objects.get(uid=user_id).bmr, tdee=user.objects.get(uid=user_id).tdee, datetime=edate, items=eitems, calories=food.objects.get(items=eitems, convenience=estore).calories, total=etotal, times=etimes)  #寫入資料庫
				unit.save()
				line_bot_api.reply_message(event.reply_token, TextSendMessage(text='您的餐點紀錄已成功輸入，輸入內容如下:'+'\n日期：'+edate+'\n時間：'+etime+'\n產品名稱：'+eitems + content))
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))

