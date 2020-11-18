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
						func.sendQuickreply(event)
					elif mtext == '@飯類':
						line_bot_api.reply_message(event.reply_token, TextSendMessage(
							text = random.choice(['全家的蒲燒鰻魚飯糰，熱量151大卡。',
							'全家的龍蝦風味細卷，熱量180大卡。','全家的火腿玉米細卷，熱量184大卡。','全家的博多明太子鮭魚飯糰，熱量171大卡。',
							'全家的雞肉飯飯糰，熱量177大卡。','全家的鹽蔥燒肉飯糰，熱量191大卡。','全家的薑燒豚肉烤飯糰，熱量195大卡。',
							'全家的蜜汁燒肉飯糰，熱量177大卡。','全家的蔥爆牛柳飯糰，熱量176大卡。','全家的泡菜燒肉飯糰，熱量179大卡。',
							'全家的鮑菇脆筍飯糰，熱量184大卡。','全家的壽喜燒牛肉飯糰，熱量196大卡。','全家的東港櫻花蝦油飯，熱量692大卡。',
							'全家的雙麥鮮蔬米漢堡，熱量302.3大卡。','全家的大飯糰鮪魚，熱量300大卡。','全家的海陸雙拼壽司組，熱量328大卡。',
							'全家的火腿玉米炒飯，熱量408大卡。','全家的肉絲蛋炒飯，熱量414大卡。','全家的大口特濃咖哩豬排飯糰，熱量339大卡。',
							'全家的香腸烤雞傳統飯糰，熱量395大卡。','全家的泡菜起司豬排黑秈飯糰，熱量340大卡。','全家的大口義式香草烤雞飯糰，熱量341大卡。',
							'全家的大口炙燒培根漢堡排飯糰，熱量388大卡。','全家的海鮮沙拉握壽司，熱量413大卡。','全家的海陸沙拉握壽司，熱量430大卡。',
							'全家的大口塔香烤雞五穀米飯糰，熱量434大卡。','全家的大口燒豚考績雙拼飯飯糰，熱量460大卡。','全家的大口宮保雞丁飯糰，熱量408大卡。',
							'全家的大口麻婆豆腐雞排飯糰，熱量429大卡。','全家的紅藜蔬食炒飯，熱量515大卡。','全家的輕鬆生活素三杯炒飯，熱量604大卡。',
							'全家的輕鬆生活蝦仁炒飯，熱量539大卡。','全家的輕鬆生活鮭魚炒飯，熱量556大卡。','全家的韓式泡菜烤肉拌飯，熱量568大卡。',
							'全家的泰式椒麻雞濃奶油燉飯，熱量568大卡。','全家的台式香腸炒飯，熱量796大卡。','全家的法式松露烤雞燉飯，熱量503大卡。','全家的新招牌炸雞腿便當，熱量574大卡。',
							'全家的黑胡椒烤雞彩便當，熱量510大卡。','全家的健身G肉餐盒，熱量446大卡。','全家的迷迭香烤雞彩便當，熱量414大卡。','全家的鐵板滑蛋豬排丼，熱量673大卡。',
							'全家的黑胡椒豬柳燴飯，熱量610大卡。','全家的沙茶豬肉燴飯，熱量702大卡。','全家的日式雞五目烤飯糰，熱量236大卡。','全家的燒肉牛五花烤飯糰，熱量233大卡。',
							'全家的明太子龍蝦風味飯糰，熱量212大卡。','全家的日式胡麻雞肉超級大麥飯糰，熱量209大卡。','全家的肉鬆飯糰，熱量245大卡。','全家的明太子龍蝦風味飯糰，熱量212大卡。',
							'全家的柴魚乳酪超級大麥飯糰，熱量242大卡。','全家的鮪魚飯糰，熱量208大卡。','全家的野郎炙燒培根卷飯糰，熱量233大卡。','全家的起司厚切豬排手卷，熱量249大卡。',
							'全家的稻荷壽司，熱量256大卡。','全家的豬排厚蛋麻婆豆腐飯糰，熱量200大卡。','全家的烤雞排厚蛋野蔬咖哩飯糰，熱量224大卡。','全家的照燒烤雞手卷，熱量229大卡。',
							'全家的大飯糰松露野菇烤雞，熱量251大卡。','全家的龍蝦風味魚卵手卷，熱量293大卡。','全家的韓式飯卷-泡菜燒肉，熱量254大卡。','全家的韓式飯卷-醬燒牛肉，熱量293大卡。',
							'全家的大飯糰辛口咖哩雞，熱量245大卡。','全家的大飯糰韓式春川辣雞，熱量279大卡。','全家的韓式飯卷-辣醬鮪魚，熱量292大卡。','全家的泰式打拋燴飯，熱量252大卡。',
							'7-11的新極上飯糰-霜降牛，熱量264大卡。','7-11的炙燒牛小排飯糰，熱量206大卡。','7-11的肉鬆飯糰，熱量210大卡。','7-11的鮪魚飯糰，熱量198大卡。',
							'7-11的博多明太子鮭魚飯糰，熱量181大卡。','7-11的黑胡椒烤豬里肌飯糰，熱量190大卡。','7-11的宗家府泡菜燒肉飯糰，熱量196大卡。','7-11的開丼握便當-麻婆烤雞腿排，熱量492大卡。',
							'7-11的鯖魚紅藜御膳便當，熱量551大卡。','7-11的明太子雞唐揚便當，熱量508大卡。','7-11的海鮮起司焗飯，熱量534大卡。','7-11的握便當-日式炸豬排丼，熱量523大卡。',
							'7-11的黑胡椒牛柳燴飯，熱量597大卡。','7-11的滑蛋雞排丼，熱量583大卡。','7-11的韓式起司炸雞炒飯，熱量587大卡。',
							'7-11的新極上飯糰-炙燒明太子，熱量198大卡。','7-11的新極上飯糰-鹽烤松阪豬，熱量198大卡。','7-11的泡菜燒肉飯卷，熱量403大卡。','7-11的炙燒雪花牛飯糰，熱量213大卡。',
							'7-11的肉鬆玉子雙手卷，熱量383大卡。','7-11的炙燒明太子鮭魚飯糰，熱量191大卡。','7-11的秋鮭鮪魚雙手卷，熱量348大卡。',
							'7-11的鹹蛋黃肉鬆飯糰，熱量274大卡。','7-11的香草烤雞蛋飯堡，熱量321大卡。','7-11的握便當-滑蛋雞排丼，熱量421大卡。','7-11的握便當-鹽烤燒肉雙拼，熱量495大卡。',
							'7-11的海鮮沙拉花壽司，熱量419大卡。','7-11的壹番屋-雙起司咖哩雞肉飯糰，熱量248大卡。','7-11的海陸雙拼壽司組，熱量490大卡。','7-11的鮭魚海帶芽飯糰，熱量187大卡。',
							'7-11的握便當-經典奮起湖，熱量389大卡。','7-11的明太子鮭魚烤飯糰，熱量205大卡。','7-11的雙蔬鮪魚飯糰，熱量209大卡。','7-11的繼光香香雞-蒜香炸雞飯糰，熱量216大卡。',
							'7-11的泰式打拋雞飯糰，熱量221大卡。','7-11的石安牧場溏心蛋筍飯飯糰，熱量182大卡。','7-11的哇沙米鮭魚飯糰，熱量212大卡。','7-11的泡菜燒肉飯糰，熱量195大卡。',
							'7-11的蔥鹽燒肉飯糰，熱量210大卡。','7-11的御選肉鬆飯糰，熱量213大卡。','7-11的雞肉飯飯糰，熱量197大卡。','7-11的魚卵小龍蝦沙拉飯糰，熱量211大卡。',
							'7-11的新極上飯糰-鮭魚鮭魚卵，熱量190大卡。','7-11的握便當-黑胡椒烤雞排，熱量380大卡。','7-11的招牌雙手卷，熱量434大卡。','7-11的海鮮雙手卷，熱量428大卡。',
							'7-11的京都豆皮壽司，熱量278大卡。','7-11的奮起湖雙拼便當，熱量656大卡。','7-11的經典排骨便當，熱量678大卡。','7-11的麻婆豆腐燴飯，熱量644大卡。',
							'7-11的經典奮起湖便當，熱量593大卡。','7-11的烤雞起司肉醬焗飯，熱量578大卡。','7-11的松露蕈菇雞肉燉飯，熱量496大卡。',
							'7-11的歐姆蛋明太子海鮮飯，熱量577大卡。','7-11的義式嫩雞花椰菜飯，熱量258大卡。','7-11的義式嫩雞花椰菜飯，熱量258大卡。','7-11的一鍋燒-日式親子丼，熱量563大卡。',
							'7-11的韓式炸雞起司丼，熱量679大卡。','7-11的歐姆蛋牛肉咖哩飯，熱量665大卡。','7-11的繽紛鮮蔬烤雞便當，熱量353大卡。','7-11的雙拼起司奶香焗飯，熱量584大卡。',
							'7-11的泰式綠咖哩飯-辣，熱量548大卡。'])))
					elif mtext == '飯類':
						dt = datetime.now().strftime('%Y-%m-%d')
						if eat.objects.filter(uid=user_id, datetime=dt).exists():
							etdee = float(eat.objects.filter(uid=user_id, datetime=dt).last().tdee)
							surplus = etdee-eat.objects.filter(uid=user_id, datetime=dt).last().total
							sp = surplus/2
							# reit_list = list(food.objects.filter(kind='飯類', calories__lte=sp).items)
							for item in food.objects.get(kind='飯類', id=220):
								line_bot_api.reply_message(event.reply_token, TextSendMessage(text='推薦給您：'+item.items))
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

