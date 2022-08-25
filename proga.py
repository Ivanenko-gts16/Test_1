import random
import telebot

HELP = """
     /help - напечатать справку по программе.
     /add - добавить задачу в список(название задачи запрашиваем у пользователя).
     /show - напечатать задачу на выбранную дату.
     /showall - напечатать все добавленные задачи
     /random - добавлять случаную задачу на дату Сегодня"""

RANDOM_TASKS= ['Записаться на курс по Python', 'Написать письмо для Андрея',
                'Покормить кошку', 'Купить машину']
tasks = {}
token = '5795484407:AAEUN_LBVnfFEjjtT5sllltL75x_lv1cOLo'
bot = telebot.TeleBot(token)

def add_task(day, task):
    if day in tasks:
        tasks[day].append(task)
    else:
        tasks[day] = [task]

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=['add'])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_task(date, task)
    bot.send_message(message.chat.id, f'Задача ""{task}" добавленна на дату "{date}"')

@bot.message_handler(commands=['random'])
def random_add(message):
    task = random.choice(RANDOM_TASKS)
    add_task('сегодня', task)
    bot.send_message(message.chat.id, f'Задача ""{task}" добавленна на дату "cегодня"')

@bot.message_handler(commands=['show'])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ''
    if date in tasks:
        text = date.upper() + '\n'
        for task in tasks[date]:
            text = text + '[]' + task + '\n'
    else:
        text = 'На данную дату нет задач!'
    bot.send_message(message.chat.id,text)


@bot.message_handler(commands=['showall'])
def show_all(message):
    #command = message.text.split(maxsplit=1)
    #date = command[1].lower()
    text = ''
    for all in tasks:
        text = all.upper() + '\n'
        for b in tasks[all]:
            text = text + '[]' + b + '\n'

    bot.send_message(message.chat.id,text)




#             a = all
#             for b in tasks[all]:
#                 print(f'На дату "{a}" имеется запись:- {b}')

# bot.message_handler(content_types=['text'])
# def echo(message):
#     if message.text == 'Серега':
#         bot.send_message(message.chat.id, 'Ба, какие люди')
#     elif message.text == 'Че делаешь?':
#         bot.send_message(message.chat.id, 'Смотрю как ты работаешь')
#     else:
#         bot.send_message(message.chat.id, 'Ты только это умеешь писать?')
bot.polling(none_stop=True)


# run = True
#


#
# while run:
#     command = input('Введите команду: ')
#     if command == 'help':
#         print(HELP)
#
#     elif command == 'show':
#         whay=input('На какую дату хотите посмотреть задачи?: ')
#         if whay in tasks:
#             for task in tasks[whay]:
#                 print('- ',task)
#         else:
#             print('На данную дату нет задач!')
#
#     elif command == 'show all':
#         for all in tasks:
#             a = all
#             for b in tasks[all]:
#                 print(f'На дату "{a}" имеется запись:- {b}')
#
#     elif command == 'add':
#         task = input('Введите название задачи: ')
#         days = input('На какой день записать?: ')
#         add_task(days, task)
#
#     elif command == 'random':
#         task = random.choice(RANDOM_TASKS)
#         add_task('Сегодня', task)
#
#     elif command == 'exit':
#         run = False
#         print('Возвращайся!=)')
#
#     else:
#         print('Научись печатать, осел!')
#         break
#
