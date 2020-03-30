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

		if event.message.text == "文字":
			line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))
			
		#line_bot_api.reply_message("1")
		#for event in events:
		#	if isinstance(event, MessageEvent):
		#		if isinstance(event.message, TextMessage):
		#			
		#			mtext = event.message.text
		#			if mtext == '女/140/40/18':
		#				func.sendText(event1)
		#			elif mtext == '好':
		#				func.sendQuickreply(event)
					
		return HttpResponse()
	else:
		return HttpResponseBadRequest()


# Create your views here.
