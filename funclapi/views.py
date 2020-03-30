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
					if mtext == '140':
						line_bot_api.reply_message(event.reply_token, TextSendMessage(text='你的基礎代謝率為1024，請回傳好。'))
					if mtext == '好':
						line_bot_api.reply_message(event.reply_token, QuickreplySendMessage(items=[
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
							]
						)
						#func.sendText(event1)
		#			elif mtext == '好':
		#				func.sendQuickreply(event)
					
		return HttpResponse()
	else:
		return HttpResponseBadRequest()


# Create your views here.
