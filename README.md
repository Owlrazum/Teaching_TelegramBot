# Телеграм бот, Python Start

Телеграм бот является финальным проектом для курса Python Start. Ниже приведён гайд, по его прохождении вы в самостоятельном плавании, при возникновении вопросов задавайте их преподавателю. В классе желательно позаниматься вместе с преподавателем на терминале.

Вам нужно будет придумать функционал для своего бота, и выбрать используемую библиотеку. Можно выбрать между [pytelegrambotapi](https://github.com/eternnoir/pyTelegramBotAPI) и [aiogram](https://docs.aiogram.dev/en/dev-3.x/). По aiogram есть крутой [гайд](https://mastergroosha.github.io/aiogram-3-guide/quickstart/)

## Гайд
Ниже приведены шаги для того чтобы запустить простого бота через быстрый, но плохой [гайд](https://habr.com/en/articles/442800/). Гайд написан с учётом того что вы на Windows, не обращайте внимания на то что скрины с MacOs

Устанавливайте программы в случае если их нет

1. Установите [Python](https://www.python.org/downloads/) версии >3.9

2. Установите [Visual Studio Code](https://code.visualstudio.com) для редактирования кода и удобства (можно там же открывать терминал и управлять контролем версий)

3. Создайте папку для проекта в удобном для вас месте, важно держать в порядке свой компьютер. На уроке папка называется 'Питон-(время группы)'

4. Через Visual Studio Code откройте папку, откройте терминал ![скриншот](/resources/terminal_1.png) В терминале напечатайте `python3 --version`. Вместо `python3` можно напечатать `python`, если у вас система позволяет.

5. Теперь приступаем к установке библиотек. Для начала создаём виртуальное окружение через `python3 -m venv .venv`. Затем устанавливаем библиотеку, которая будет локальной для этой папки: `\.venv\Scripts\python -m pip install pytelegrambotapi`

6. Теперь в своей папке, но не в .venv, создаём файл `main.py` и вставляем туда нижеследующий код: Вместо `Вставьте токен в эту строку` вам надо вставить свой токен, в 7 шаге показывается как получить токен.

```
import telebot;
from telebot import types
bot = telebot.TeleBot('Вставьте свой токен в эту строку');


name = '';
surname = '';
age = 0;
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?");
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg');

def get_name(message): #получаем фамилию
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?');
    bot.register_next_step_handler(message, get_surname);

def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message(message.from_user.id, 'Сколько тебе лет?');
    bot.register_next_step_handler(message, get_age);

def get_age(message):
    global age;
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    bot.send_message(message.from_user.id, 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?')

bot.polling(none_stop=True, interval=0)
```

Этот код является финальным для этого [гайда](https://habr.com/en/articles/442800/)

7. Для того чтобы получить токен для своего бота от Телеграмма, вам надо найти @BotFather и следовать его инструкциям. В качестве ника рекомендую `Algo_py_name_o23`, где вместо name ваше имя или ник. Он пришлёт вам токен который вы должны взять отсюда ![скрин](/resources/botfather.png)
