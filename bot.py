import telebot
from lists_hubs import stikers_hub, hehe_hub #list_matov
from day_until_NY import day_rem
import random
import json
from weather import act_temperature
from news import gen_news
#from news_reuters import gen_news_en

token = "0000"

bot = telebot.TeleBot(token)


# команда для тех, кто предпочитает "/"" для добавления шутки
@bot.message_handler(commands=["joke"])
def joke(message):
    your_joke = bot.reply_to(message, "Расскажи мне шутку, негодник)")
    bot.register_next_step_handler(your_joke, add_joke)


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, """Саламуля, я умею:
1) По команде /joke или на ввод сообщения "хочу добавить шутку" добавлять ваши шутки в своей блокнотик
2) Шутить на ввод сообщения "расскажи шутку" или "расскажи анекдот"
3) Реагировать на ваши мемы
4) Рассказать новости на ввод сообщения "расскажи новости"
5) Сказать актуальную погоду на ввод сообщения "скажи погоду" или "какая погода""")
# функция, добавляющая шутку в json


def add_joke(message):
    message_for_add = message.text
    print(message_for_add)
    with open("data_jokes.json", encoding="UTF-8") as f:
        records = json.load(f)
        print(records)
        count = len(records)
        records[str(count)] = message_for_add
        print(records)
    with open('data_jokes.json', 'w', encoding='UTF-8') as file_out:
        json.dump(records, file_out, ensure_ascii=False, indent=2)

    bot.send_message(message.chat.id, "Записал в свой блокнотик")

    # for i in list_matov:
    #     if i in message.text.lower():      <---- здесь был обработчик матов, но пользователям не понравилось :(
    #         bot.send_message(message.chat.id, "Без матов!!!")


# основной блок, который позволяет взаимодействовать без "/"
@bot.message_handler(content_types=["text"])
def echo(message):
    if "дней до" in message.text.lower() or "осталось до" in message.text.lower():
        if "нового года" in message.text.lower() or "нг" in message.text.lower():
            bot.send_message(message.chat.id, day_rem)
            random_stiker = stikers_hub[random.randint(
                0, len(stikers_hub) - 1)]
            bot.send_sticker(message.chat.id, random_stiker)
    if "шутку" in message.text.lower() or "расскажи анек" in message.text.lower():
        with open('bot_work', encoding='UTF-8') as f:
            records = json.load(f)
            rand_number = random.randint(0, len(records))

            rand_joke = records[str(rand_number)]
            bot.send_message(message.chat.id, rand_joke)
    if "хочу добавить шутку" in message.text.lower():
        your_joke = bot.reply_to(message, "Расскажи мне шутку, негодник)")
        bot.register_next_step_handler(your_joke, add_joke)
    if "скажи погоду" in message.text.lower() or "какая погода" in message.text.lower():
        bot.send_message(message.chat.id, act_temperature())
    if "расскажи новости" in message.text.lower():
        bot.send_message(message.chat.id, gen_news())
    #if "расскажи вражеские новости" in message.text.lower():
    #   bot.send_message(message.chat.id, gen_news_en())


# для реакции на фото пользователей
@bot.message_handler(content_types=['photo'])
def photo_id(message):

    random_hehe = hehe_hub[random.randint(0, len(hehe_hub) - 1)]
    bot.send_message(message.chat.id, random_hehe)


bot.polling(none_stop=True)
