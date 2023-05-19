import json
import telebot

with open('tokens.json') as file:
    data = json.load(file)

bots = []
for account in data:
    token = account['token']
    bot = telebot.TeleBot(token)
    bots.append(bot)


@bots[0].message_handler(commands=['join'])
def join_group(message):
    chat_id = message.chat.id
    group_id = '<YOUR_GROUP_ID>'  # استبدل <YOUR_GROUP_ID> بمعرف المجموعة المستهدفة

    
    try:
        bots[0].add_chat_member(group_id, chat_id)
        bots[0].send_message(chat_id, 'تمت إضافتك إلى المجموعة بنجاح!')
    except Exception as e:
        bots[0].send_message(chat_id, f'حدث خطأ: {str(e)}')

# استبدال الرقم الذي تحتاجه في حالة وجود حسابات إضافية
@bots[1].message_handler(commands=['join'])
def join_group2(message):
    # العمليات المطلوبة هنا

# استكمال العمليات لباقي الحسابات إذا لزم الأمر


for bot in bots:
	bot.polling()
