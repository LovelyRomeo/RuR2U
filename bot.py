import requests

proxy = {
    'http': 'rur2u.ru:80',
}
   
try:
    response = requests.get('https://api.openai.com', proxies=proxy)
    print("Connection successful")
except requests.exceptions.RequestException:
    print("Connection failed")


client = OpenAI(api_key='')

def gpt(text):
    completion = client.chat.completions.create(
    model = 'gpt-3.5-turbo',
    messages = [
        {"role": "system", "content" : "You are a bot assistant imitating a real person."},
        {'role': 'user', 'content': f'{text}'}
    ],
    temperature = 0.5
    )
    
    english_text = completion.choices[0].message.content
    
    return english_text


bot = telebot.TeleBot('6830160847:AAFFkCXdTAXsI8dj2A3PGk71XloMfmtUxdw')



url="https://rur2u.ru"

@bot.message_handler(commands=['start'])
def start(message):
    info = types.InlineKeyboardMarkup()
    webAppTest = types.WebAppInfo(url)
    info.add(types.InlineKeyboardButton('Открыть ▶️RuR2U🇷🇺', web_app=webAppTest))
    info.add(types.InlineKeyboardButton('Открыть 💬RuR2U AI', callback_data='AI'))
    bot.send_message(message.chat.id, 'Добро пожаловать в RuR🤩\n\n😍🇷🇺 RuR2U - первое приложение в Телеграм про Росиию!\n\n▶️ Что бы запустить приложение, нажмите кнопку START внизу!\n\nRuR2U - это:\n🔹Полезная информация про Россию\n🔹Афиша мероприятий\n🔹Скидки от крутых и популярных сервисов и компаний\n🔹Рестораны города\n🔹Свежие новости\n🔹Интересные Квизы\n🔹Розыгрыши подарков\nи многое-многое другое!\n\nЗапускайте приложение и насладитесь RuR2U прямо сейчас \n🔽🔽🔽', reply_markup=info)

@bot.callback_query_handler(func=lambda calback: True)
def callback_message(callback):
    if callback.data == 'AI':
        bot.send_message(callback.message.chat.id, 'Добрый день!\nЯ искусстенный интеллект RuR2U и готов ответить на все ваши вопросы про Россию🇷🇺.\n\nКакой у вас вопрос?')


@bot.message_handler()
def ai(message):
    bot.send_message(message.chat.id, 'Генерируется ответ♻️🧠')
    bot.send_message(message.chat.id, f'{gpt(message)}')
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id + 1) 


bot.polling(none_stop=True)
