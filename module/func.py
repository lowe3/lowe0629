from django.conf import settings
import datetime
from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction, ButtonsTemplate, URITemplateAction, ConfirmTemplate, PostbackTemplateAction, TemplateSendMessage
import random
from funclapi.models import wefamily, user, food, eat

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def sendImage(event):
	try:
		message = ImageSendMessage(
			original_content_url = "https://imgur.com/eIejLVQ.jpg",preview_image_url = "https://imgur.com/eIejLVQ.jpg"
		)
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
		
def sendQuickreply(event):  #快速選單
    try:
        message = TextSendMessage(
            text='請選擇您現在想吃的種類',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="飯類", text="@飯類")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="麵類", text="@麵類")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="沙拉", text="@沙拉")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="麵包", text="@麵包")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="飲料", text="@飲料")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="關東煮", text="@關東煮")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="甜點", text="@甜點")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="湯類", text="@湯類")
                    ),	
                    QuickReplyButton(
                        action=MessageAction(label="水果", text="@水果")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="醬料", text="@醬料")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="其他", text="@其他")
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
		eitems = flist[4]
		for fitems in food.objects.filter(items=eitems):
			content='\n熱量:'+str(fitems.calories)+'大卡'
			if not (eat.objects.filter(uid=user_id, datetime=edate).exists()):
			# timess = int(1)
				unit = eat.objects.create(uid=user_id, bmr=user.objects.get(uid=user_id).bmr, tdee=user.objects.get(uid=user_id).tdee, datetime=edate, items=eitems, calories=fitems.calories, total=fitems.calories, times=1)  #寫入資料庫
			# unit = eat.objects.create(uid=user_id, bmr=user.objects.get(uid=user_id).bmr, tdee=user.objects.get(uid=user_id).tdee, datetime=edatetime, items=eitems, calories=fitems.calories)  #寫入資料庫
				unit.save()
				line_bot_api.reply_message(event.reply_token, TextSendMessage(text='您的餐點紀錄已成功輸入，輸入內容如下:'+'\n日期:'+edate+'\n時間：'+etime+'\n產品名稱：'+eitems +content))
			else:
				# etotal = eat.objects.filter(uid=user_id, datetime=edate).last().total + food.objects.filter(items=eitems).calories
				# etimes = eat.objects.filter(uid=user_id, datetime=edate).last().times + 1
				etotal = eat.objects.filter(uid=user_id, datetime=edate).last()
				# etimes = eat.objects.filter(uid=user_id, datetime=edate).latest('times') + 1
				# eunit = eat.objects.create(uid=user_id, bmr=user.objects.get(uid=user_id).bmr, tdee=user.objects.get(uid=user_id).tdee, datetime=edate, items=eitems, calories=fitems.calories, total=etotal, times=etimes)  #寫入資料庫
				# eunit.save()
				line_bot_api.reply_message(event.reply_token, TextSendMessage(text=etotal))
				# line_bot_api.reply_message(event.reply_token, TextSendMessage(text='您的餐點紀錄已成功輸入，輸入內容如下:'+'\n日期時間：'+edate+etime+'\n產品名稱：'+eitems+content+etotal))
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))

