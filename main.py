import requests
from bs4 import BeautifulSoup as b
import random
import telebot

API_KEY = '5867934782:AAGrVyjbSHI7Zxzdiaeuc-5ooyO7e-jy1kw' 
URL = 'https://www.anekdot.ru/last/good/'

def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    req = soup.find_all('div', class_='text')
    return [c.text for c in req]

list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, 'Чтобы посмеяться, введи любую цифру')

@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() in '123456789':
            bot.send_message(message.chat.id, list_of_jokes[0])
            del list_of_jokes[0]
    else:
            bot.send_message(message.chat.id, 'Введи цифру!!!')





bot.polling()