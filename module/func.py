from django.conf import settings

from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction, ButtonsTemplate, URITemplateAction, ConfirmTemplate, PostbackTemplateAction, TemplateSendMessage
import random
from funclapi.models import user, seven, wefamily

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
		text='請選擇您的運動頻率',
		quick_reply=QuickReply(
			items=[
				QuickReplyButton(
				action=MessageAction(label="久坐",text="@久坐")
			),  
				QuickReplyButton(
				action=MessageAction(label="每周有輕鬆的運動3-5天",text="@輕鬆運動3-5天")
			), 
				QuickReplyButton(
				action=MessageAction(label="每周有中等強度的運動3-5天",text="@中等運動3-5天")
			), 
				QuickReplyButton(
				action=MessageAction(label="每周有高強度的運動6-7天",text="@高度運動6-7天")
			), 
				QuickReplyButton(
				action=MessageAction(label="勞力密集的工作或每天訓練",text="@一天訓練兩次")
				),
			]))
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
		
def manageForm(event, mtext, user_id):  #處理LIFF傳回的FORM資料
    try:
        flist = mtext[3:].split("\r")  #去除前三個「#」字元再分解字串
        pheight = flist[0]  #取得輸入資料
        pweight = flist[1]
        page	= flist[2]
        pgender = flist[3]
		pbmr = flist[5]
		ptdee = flist[6]
        unit = user.objects.create(uid=user_id, height=pheight, weight=pweight, age=page, gender=pgender, bmr=pbmr, tdee=ptdee)  #寫入資料庫
        unit.save()
        text1 = "您的個人資料如下："
        text1 += "\n身高：" + pheight
        text1 += "\n體重：" + pweight
        text1 += "\n年齡：" + page
        text1 += "\n性別：" + pgender
		text1 += "\n基礎代謝率：" + pbmr
		text1 += "\n每日總消耗熱量：" + ptdee
        message = TextSendMessage(  #顯示訂房資料
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))