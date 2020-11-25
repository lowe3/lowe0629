from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from .models import user, wefamily, food, eat
from datetime import datetime, timedelta
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, TextMessage
from module import func
from linebot.models import *
from funclapi.models import user, wefamily, food, eat
from decimal import Decimal
import random
from random import choice


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
					user_id = event.source.user_id
					if not (user.objects.filter(uid=user_id).exists()):
						unit = user.objects.create(uid=user_id)
						unit.save()	
					mtext = event.message.text
					if mtext == '推薦菜單':
					message = TextSendMessage(
						text='請選擇您現在想吃的種類',
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
						dt = datetime.now().strftime('%Y-%m-%d')
						if eat.objects.filter(uid=user_id, datetime=dt).exists():
							ttotal = str(eat.objects.filter(uid=user_id, datetime=dt).last().total)
							line_bot_api.reply_message(event.reply_token, TextSendMessage(text='您今日已攝取熱量：'+ttotal+'大卡'), message)
						else:
							line_bot_api.reply_message(event.reply_token, TextSendMessage(text='您今日尚未飲食，熱量：0大卡', message))
							# func.sendQuickreply(event)
					elif mtext == '飯類':
						dt = datetime.now().strftime('%Y-%m-%d')
						if eat.objects.filter(uid=user_id, datetime=dt).exists():
							etdee = float(eat.objects.filter(uid=user_id, datetime=dt).last().tdee)
							surplus = etdee-eat.objects.filter(uid=user_id, datetime=dt).last().total
							sp = surplus/2
							if surplus < 151:
								line_bot_api.reply_message(event.reply_token, TextSendMessage(text='根據您今天的飲食狀況，已不再適合攝取飯類食物喔~'))
							else:
								item = food.objects.filter(kind=mtext, calories__lte=sp)
								rice = choice(item)
								line_bot_api.reply_message(event.reply_token, TextSendMessage(text='推薦給您：'+rice.convenience+'的'+rice.items))
						else :
							item = food.objects.filter(kind=mtext)
							ri = choice(item)
							line_bot_api.reply_message(event.reply_token, TextSendMessage(text='推薦給您：'+ri.convenience+'的'+ri.items))
					elif mtext == '麵類':
						dt = datetime.now().strftime('%Y-%m-%d')
						if eat.objects.filter(uid=user_id, datetime=dt).exists():
							etdee = float(eat.objects.filter(uid=user_id, datetime=dt).last().tdee)
							surplus = etdee-eat.objects.filter(uid=user_id, datetime=dt).last().total
							sp = surplus/2
							if surplus < 162:
								line_bot_api.reply_message(event.reply_token, TextSendMessage(text='根據您今天的飲食狀況，已不再適合攝取麵類食物喔~'))
							else:
								item = food.objects.filter(kind=mtext, calories__lte=sp)
								noo = choice(item)
								line_bot_api.reply_message(event.reply_token, TextSendMessage(text='推薦給您：'+noo.convenience+'的'+noo.items))
						else :
							item = food.objects.filter(kind=mtext)
							noodle = choice(item)
							line_bot_api.reply_message(event.reply_token, TextSendMessage(text='推薦給您：'+noodle.convenience+'的'+noodle.items))
					elif mtext == '沙拉':
						dt = datetime.now().strftime('%Y-%m-%d')
						if eat.objects.filter(uid=user_id, datetime=dt).exists():
							etdee = float(eat.objects.filter(uid=user_id, datetime=dt).last().tdee)
							surplus = etdee-eat.objects.filter(uid=user_id, datetime=dt).last().total
							sp = surplus/2
							if surplus < 32:
								line_bot_api.reply_message(event.reply_token, TextSendMessage(text='根據您今天的飲食狀況，已不再適合吃沙拉喔~'))
							else:
								item = food.objects.filter(kind=mtext, calories__lte=sp)
								sal = choice(item)
								line_bot_api.reply_message(event.reply_token, TextSendMessage(text='推薦給您：'+sal.convenience+'的'+sal.items))
						else :
							item = food.objects.filter(kind=mtext)
							salad = choice(item)
							line_bot_api.reply_message(event.reply_token, TextSendMessage(text='推薦給您：'+salad.convenience+'的'+salad.items))
					elif mtext == '麵包':
						dt = datetime.now().strftime('%Y-%m-%d')
						if eat.objects.filter(uid=user_id, datetime=dt).exists():
							etdee = float(eat.objects.filter(uid=user_id, datetime=dt).last().tdee)
							surplus = etdee-eat.objects.filter(uid=user_id, datetime=dt).last().total
							sp = surplus/2
							if surplus < 93:
								line_bot_api.reply_message(event.reply_token, TextSendMessage(text='根據您今天的飲食狀況，已不再適合吃麵包喔~'))
							else:
								item = food.objects.filter(kind=mtext, calories__lte=sp)
								bre = choice(item)
								line_bot_api.reply_message(event.reply_token, TextSendMessage(text='推薦給您：'+bre.convenience+'的'+bre.items))
						else :
							item = food.objects.filter(kind=mtext)
							bread = choice(item)
							line_bot_api.reply_message(event.reply_token, TextSendMessage(text='推薦給您：'+bread.convenience+'的'+bread.items))		
					elif mtext == '飲料':
						dt = datetime.now().strftime('%Y-%m-%d')
						if eat.objects.filter(uid=user_id, datetime=dt).exists():
							etdee = float(eat.objects.filter(uid=user_id, datetime=dt).last().tdee)
							surplus = etdee-eat.objects.filter(uid=user_id, datetime=dt).last().total
							sp = surplus/2
							item = food.objects.filter(kind=mtext, calories__lte=sp)
							dri = choice(item)
							line_bot_api.reply_message(event.reply_token, TextSendMessage(text='推薦給您：'+dri.convenience+'的'+dri.items+'，但為了您的身體健康著想，還是希望您喝水。'))
						else :
							item = food.objects.filter(kind=mtext)
							drink = choice(item)
							line_bot_api.reply_message(event.reply_token, TextSendMessage(text='推薦給您：'+drink.convenience+'的'+drink.items+'，但為了您的身體健康著想，還是希望您喝水。'))
					elif mtext == '關東煮':
						dt = datetime.now().strftime('%Y-%m-%d')
						if eat.objects.filter(uid=user_id, datetime=dt).exists():
							etdee = float(eat.objects.filter(uid=user_id, datetime=dt).last().tdee)
							surplus = etdee-eat.objects.filter(uid=user_id, datetime=dt).last().total
							sp = surplus/2
							if surplus < 5:
								line_bot_api.reply_message(event.reply_token, TextSendMessage(text='根據您今天的飲食狀況，已不再適合吃關東煮喔~'))
							else:
								item = food.objects.filter(kind=mtext, calories__lte=sp)
								kt = choice(item)
								line_bot_api.reply_message(event.reply_token, TextSendMessage(text='推薦給您：'+kt.convenience+'的'+kt.items))
						else :
							item = food.objects.filter(kind=mtext)
							ktc = choice(item)
							line_bot_api.reply_message(event.reply_token, TextSendMessage(text='推薦給您：'+ktc.convenience+'的'+ktc.items))
					elif mtext == '甜點':
						dt = datetime.now().strftime('%Y-%m-%d')
						if eat.objects.filter(uid=user_id, datetime=dt).exists():
							etdee = float(eat.objects.filter(uid=user_id, datetime=dt).last().tdee)
							surplus = etdee-eat.objects.filter(uid=user_id, datetime=dt).last().total
							sp = surplus/2
							if surplus < 146:
								line_bot_api.reply_message(event.reply_token, TextSendMessage(text='根據您今天的飲食狀況，已不再適合吃甜點喔~'))
							else:
								item = food.objects.filter(kind=mtext, calories__lte=sp)
								swe = choice(item)
								line_bot_api.reply_message(event.reply_token, TextSendMessage(text='推薦給您：'+swe.convenience+'的'+swe.items))
						else :
							item = food.objects.filter(kind=mtext)
							sweat = choice(item)
							line_bot_api.reply_message(event.reply_token, TextSendMessage(text='推薦給您：'+sweat.convenience+'的'+sweat.items))
					elif mtext == '湯類':
						dt = datetime.now().strftime('%Y-%m-%d')
						if eat.objects.filter(uid=user_id, datetime=dt).exists():
							etdee = float(eat.objects.filter(uid=user_id, datetime=dt).last().tdee)
							surplus = etdee-eat.objects.filter(uid=user_id, datetime=dt).last().total
							sp = surplus/2
							if surplus < 86:
								line_bot_api.reply_message(event.reply_token, TextSendMessage(text='根據您今天的飲食狀況，已不再適合喝湯喔~'))
							else:
								item = food.objects.filter(kind=mtext, calories__lte=sp)
								sou = choice(item)
								line_bot_api.reply_message(event.reply_token, TextSendMessage(text='推薦給您：'+sou.convenience+'的'+sou.items))
						else :
							item = food.objects.filter(kind=mtext)
							soup = choice(item)
							line_bot_api.reply_message(event.reply_token, TextSendMessage(text='推薦給您：'+soup.convenience+'的'+soup.items))
					elif mtext == '水果':
						dt = datetime.now().strftime('%Y-%m-%d')
						if eat.objects.filter(uid=user_id, datetime=dt).exists():
							etdee = float(eat.objects.filter(uid=user_id, datetime=dt).last().tdee)
							surplus = etdee-eat.objects.filter(uid=user_id, datetime=dt).last().total
							sp = surplus/2
							if surplus < 55:
								line_bot_api.reply_message(event.reply_token, TextSendMessage(text='根據您今天的飲食狀況，已不再適合吃水果喔~'))
							else:
								item = food.objects.filter(kind=mtext, calories__lte=sp)
								fru = choice(item)
								line_bot_api.reply_message(event.reply_token, TextSendMessage(text='推薦給您：'+fru.convenience+'的'+fru.items))
						else :
							item = food.objects.filter(kind=mtext)
							fruit = choice(item)
							line_bot_api.reply_message(event.reply_token, TextSendMessage(text='推薦給您：'+fruit.convenience+'的'+fruit.items))	
					elif mtext == '其他':
						dt = datetime.now().strftime('%Y-%m-%d')
						if eat.objects.filter(uid=user_id, datetime=dt).exists():
							etdee = float(eat.objects.filter(uid=user_id, datetime=dt).last().tdee)
							surplus = etdee-eat.objects.filter(uid=user_id, datetime=dt).last().total
							sp = surplus/2
							if surplus < 33:
								line_bot_api.reply_message(event.reply_token, TextSendMessage(text='根據您今天的飲食狀況，已不再適合吃這類的食物喔~'))
							else:
								item = food.objects.filter(kind=mtext, calories__lte=sp)
								oth = choice(item)
								line_bot_api.reply_message(event.reply_token, TextSendMessage(text='推薦給您：'+oth.convenience+'的'+oth.items))
						else :
							item = food.objects.filter(kind=mtext)
							other = choice(item)
							line_bot_api.reply_message(event.reply_token, TextSendMessage(text='推薦給您：'+other.convenience+'的'+other.items))						
					elif mtext[:3] == '$$$':  #處理LIFF傳回的FORM資料
						func.manageForm(event, mtext, user_id)
					elif mtext == '餐點紀錄':
						line_bot_api.reply_message(event.reply_token, TextSendMessage(text='https://liff.line.me/1654959608-r96wdMBL'))
					# elif mtext[-2:] == '公分':
						# he = int(''.join([x for x in mtext if x.isdigit()]))
						# hhe = '%d'%he
						# line_bot_api.reply_message(event.reply_token, TextSendMessage(text='您的身高是'+hhe+'公分，請輸入您的體重，EX:50公斤'))
					elif mtext == '基本資料':
						line_bot_api.reply_message(event.reply_token, TextSendMessage(text='https://liff.line.me/1654777422-nzqQ2eyK'))
					elif mtext == '食物熱量查詢':
						line_bot_api.reply_message(event.reply_token, TextSendMessage(text='可直接輸入欲查詢之食物，也可點擊下面網址查詢：'+ '\n' + 'https://liff.line.me/1655188974-Jd80vNk8'))						
					elif mtext == '飲食小知識':
						line_bot_api.reply_message(event.reply_token, TextSendMessage(
							text = random.choice(['不要忘記吃早餐，通過每天早晨所吃下的早餐，才能提供足夠的能量與營養面對一天工作的挑戰。',
							'少喝奶茶。因為高熱量、高油、沒有營養價值可言。長期飲用，易罹患高血壓、糖尿病等疾病。',
							'睡前三小時不要吃東西。會胖。',
							'早餐可以選擇健康的全麥穀物、牛奶、蛋、粥和「較清淡」的食物，以及一些新鮮水果和足夠的水。',
							'建議每週至少吃兩次魚類或其他海鮮，特別像是鮭魚、鱒魚、沙丁魚、鯡魚和金槍魚等油性魚類，擁有較高的ω-3脂肪含量，對於人體是不可或缺的營養素，因此千萬不要忽略魚肉及海鮮的重要。',
							'健康的零食，像是：水果，無鹽堅果，減脂牛奶或酸奶等，或是一些健康品牌銷售的代糖點心、蛋白棒、纖維棒等。',
							'善用蛋白質、薑素、黃酮類提升「攝食產熱效應」',
							'中國的古人認為，味覺有五種：酸甜苦辣鹹！事實上卻是，辣並非味覺而是痛覺，味覺有四種：苦酸甜鹹。',
							'蘋果中所具的有天然的香氣，對於人體來說，有舒緩壓力、提神醒腦的功效，而蘋果中充足的礦物質硼，也同樣可以使睏倦的大腦快速恢復到清醒狀態。喝杯咖啡不如吃個蘋果的道理就在於此。',
							'番茄醬是現代人的常見食品之一，但在19世紀，番茄醬並不是食品而是藥品。現代醫學研究表明，番茄醬可以有效降低人體低密度脂蛋白膽固醇的含量，從而減少心臟病和中風的危險。',
							'飲食應依『每日飲食指南』的食物分類與建議份量，適當選擇搭配。特別注意應吃到足夠量的蔬菜、水果、全穀、豆類、堅果種子及乳製品。',
							'了解自己的健康體重和熱量需求，適量飲食，以維持體重在正常範圍內。',
							'三餐應以全穀雜糧為主食。',
							'多蔬食少紅肉，多粗食少精製。',
							'飲食多樣化，選擇當季在地食材。'])))
					elif mtext == '呼叫圖表':
						line_bot_api.reply_message(event.reply_token, TextSendMessage(text='https://liff.line.me/1655267954-z4Z53lAZ'))
					elif mtext[:3] == '###':  #處理LIFF傳回的FORM資料
						flist = mtext[3:].split()
						pheight = flist[0]  #取得輸入資料
						pweight = flist[1]
						page = flist[2]
						pgender = flist[3]
						pbmr = flist[5]
						ptdee = flist[6]
						user_id = event.source.user_id
						if user.objects.get(uid=user_id):
							user.objects.filter(uid=user_id).update(height=pheight, weight=pweight, age=page, gender=pgender, bmr=pbmr[:7], tdee=ptdee[:7])  #寫入資料庫
							line_bot_api.reply_message(event.reply_token, TextSendMessage(text='您的基本資料已成功輸入，輸入內容如下:'+'\n身高：'+pheight+'\n體重：'+ pweight+'\n年齡：' + page+'\n性別：' + pgender+'\n基礎代謝率：' + pbmr[:7]+'\n每日總消耗熱量：' + ptdee[:7]))
					elif food.objects.filter(items__contains=mtext).exists():
						for fitems in food.objects.filter(items__contains=mtext):
							line_bot_api.reply_message(event.reply_token, TextSendMessage(text='品名:' + fitems.items + '\n熱量:' + str(fitems.calories) + '大卡\n圖片:' + fitems.picture + '\n超商:' + fitems.convenience + '\n種類:' + fitems.kind))							

					else :
						line_bot_api.reply_message(event.reply_token, TextSendMessage(text='回傳錯誤'))						
		return HttpResponse()
	else:
		return HttpResponseBadRequest()

