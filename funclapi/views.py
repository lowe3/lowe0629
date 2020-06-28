from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage
from module import func
from linebot.models import *

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECERT)




@csrf_exempt
def callback(request):
	if request.method == 'POST':
		signature = request.META['HTTP_X_LINE_SIGNATURE']
		body = request.body.decode('utf-8')
		
		try:
			events = parser.parse(body, signature)
		except InvalidSignatureError:
			return HttpResponseForbidden()
		except LineBotApiError:
			return HttpResponseBadRequest()
			
		
			
		for event in events:
			if isinstance(event, MessageEvent):
				if isinstance(event.message, TextMessage):
					#line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))
					mtext = event.message.text
					if mtext == '女/140/40/18':						
						line_bot_api.reply_message(event.reply_token, TextSendMessage(text='你的基礎代謝率為1024，請回傳好。'))
					elif mtext == '男/180/70/18':
						line_bot_api.reply_message(event.reply_token, TextSendMessage(text='你的基礎代謝率為1740，請回傳好。'))						
					elif mtext == '好':
						func.sendQuickreply(event)
					elif mtext == '久坐':
						line_bot_api.reply_message(event.reply_token, TextSendMessage(text='你的每日總消耗熱量為基礎代謝率*1.2。'))
					elif mtext == '每周有輕鬆的運動3-5天':
						line_bot_api.reply_message(event.reply_token, TextSendMessage(text='你的每日總消耗熱量為基礎代謝率*1.375。'))
					elif mtext == '每周有中等強度的運動3-5天':
						line_bot_api.reply_message(event.reply_token, TextSendMessage(text='你的每日總消耗熱量為基礎代謝率*1.55。'))
					elif mtext == '每周有高強度的運動6-7天':
						line_bot_api.reply_message(event.reply_token, TextSendMessage(text='你的每日總消耗熱量為基礎代謝率*1.725。'))
					elif mtext == '勞力密集的工作或每天訓練甚至一天訓練兩次':
						line_bot_api.reply_message(event.reply_token, TextSendMessage(text='你的每日總消耗熱量為基礎代謝率*1.9。'))						
					else :
						line_bot_api.reply_message(event.reply_token, TextSendMessage(text='回傳錯誤'))						
		return HttpResponse()
	else:
		return HttpResponseBadRequest()
					
# Create your views here.
