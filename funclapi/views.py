from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage
from module import func
from linebot.models import *
import random
import os
import psycopg2

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
					line_id = event.source.user_id
					mtext = event.message.text
					if mtext == '好':
						func.sendQuickreply(event)
					elif mtext[-2:] == '公分':
						he = int(''.join([x for x in mtext if x.isdigit()]))
						hhe = '%d'%he
						line_bot_api.reply_message(event.reply_token, TextSendMessage(text='您的身高是'+hhe+'公分，請輸入您的體重，EX:50公斤'))
					elif mtext[-2:] == '公斤':
						we = int(''.join([x for x in mtext if x.isdigit()]))
						wwe = '%d'%we
						line_bot_api.reply_message(event.reply_token, TextSendMessage(text='您的體重是'+wwe+'公斤，請輸入您的年齡，EX：18歲'))
					elif mtext[-1] == '歲':
						ye = int(''.join([x for x in mtext if x.isdigit()]))
						yye = '%d'%ye
						line_bot_api.reply_message(event.reply_token, TextSendMessage(text='您的年齡是'+yye+'歲，請輸入您的性別，EX：男性'))
					elif mtext == '男':
						line_bot_api.reply_message(event.reply_token, TextSendMessage(text='好的先生，接下來請選擇您的運動頻率，好嗎?'))
					elif mtext == '女':
						line_bot_api.reply_message(event.reply_token, TextSendMessage(text='好的小姐，接下來請選擇您的運動頻率，好嗎?'))
					elif mtext == '推薦菜單':
						func.sendImage(event)						
					elif mtext == '@久坐':
						line_bot_api.reply_message(event.reply_token, TextSendMessage(text='你的每日總消耗熱量為基礎代謝率*1.2。'))
					elif mtext == '@輕鬆運動3-5天':
						line_bot_api.reply_message(event.reply_token, TextSendMessage(text='你的每日總消耗熱量為基礎代謝率*1.375。'))
					elif mtext == '@中等運動3-5天':
						line_bot_api.reply_message(event.reply_token, TextSendMessage(text='你的每日總消耗熱量為基礎代謝率*1.55。'))
					elif mtext == '@高度運動6-7天':
						line_bot_api.reply_message(event.reply_token, TextSendMessage(text='你的每日總消耗熱量為基礎代謝率*1.725。'))
					elif mtext == '@一天訓練兩次':
						line_bot_api.reply_message(event.reply_token, TextSendMessage(text='你的每日總消耗熱量為基礎代謝率*1.9。'))	
					elif mtext == '飲食小知識':
						line_bot_api.reply_message(event.reply_token, TextSendMessage(
							text = random.choice(['常吃宵夜對胃產生不好的影響，因為胃一整天都得不到休息。',
							'每天早晨醒後，可以先喝一杯白開水，這樣可以預防膽結石。',
							'睡前三小時不要吃東西。會胖。',
							'中國的古人認為，味覺有五種：酸甜苦辣鹹！事實上卻是，辣並非味覺而是痛覺，味覺有四種：苦酸甜鹹。',
							'蘋果中所具的有天然的香氣，對於人體來說，有舒緩壓力、提神醒腦的功效，而蘋果中充足的礦物質硼，也同樣可以使睏倦的大腦快速恢復到清醒狀態。喝杯咖啡不如吃個蘋果的道理就在於此。',
							'番茄醬是現代人的常見食品之一，但在19世紀，番茄醬並不是食品而是藥品。現代醫學研究表明，番茄醬可以有效降低人體低密度脂蛋白膽固醇的含量，從而減少心臟病和中風的危險。',
							'飲食應依『每日飲食指南』的食物分類與建議份量，適當選擇搭配。特別注意應吃到足夠量的蔬菜、水果、全穀、豆類、堅果種子及乳製品。',
							'了解自己的健康體重和熱量需求，適量飲食，以維持體重在正常範圍內。',
							'三餐應以全穀雜糧為主食。',
							'多蔬食少紅肉，多粗食少精製。',
							'飲食多樣化，選擇當季在地食材。'])))

					else :
						line_bot_api.reply_message(event.reply_token, TextSendMessage(text='回傳錯誤'))						
		return HttpResponse()
	else:
		return HttpResponseBadRequest()
					
# Create your views here.
int(filter(str.isdigit, mtext))