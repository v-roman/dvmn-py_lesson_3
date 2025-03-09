import os
from dotenv import load_dotenv
from pathlib import Path
import smtplib

print(os.environ['LOGIN'])
dotenv_path = Path('path/to/.env')
load_dotenv(dotenv_path=dotenv_path)
frand_name = ('Денис')
sender = ('Владимир')
web_sait_name = ('https://dvmn.org/profession-ref-program/vova.romanovich.2001/kT3tm/')
text = ('''
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
''')
text = text.replace('%website%',web_sait_name)
text = text.replace('%friend_name%', frand_name)
text = text.replace('%my_name%', sender)
letter  = '''
From: v.romanov.01@yandex.by
To: v.romanov.01@yandex.by
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";
{0}'''.format(text)
letter = letter.encode("UTF-8")
print(letter)
server = smtplib.SMTP_SSL('smtp.yandex.by', 465)
server.login('LOGIN', 'PASSWORD')
server.sendmail('v.romanov.01@yandex.by', 'v.romanov.01@yandex.by', letter)
server.quit()