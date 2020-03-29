from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage
from module import func

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECERT)


@csrf_exempt
def handle_message(event):
    # 取得使用者的ID，使用者ID 與 給別人加好友的Line ID不同
    user_id = event.source.user_id

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
				mtext = event.message.text
				if mtext == '女/140/40/18':
					func.sendText(event1),
				elif mtext == '好':
					func.sendQuickreply(event),
			return HttpResponse()
	else:
		return HttpResponseBadRequest()


# Create your views here.
