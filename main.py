# -*- coding: utf-8 -*-
from SexEnum import SexEnum
from DataValidator import *
from datetime import datetime
import os


def get_reactivity_level(level: int) -> str:
    if level in range(0, 4):
        return 'низкий'
    if level in range(4, 8):
        return 'средний'
    return 'высокий'


def get_age(el: SexEnum) -> str:
    if el == SexEnum.MALE:
        return 'мужской'
    return 'женский'


questions = [
    'Вы обжигаетесь горячим чаем?',
    'Сильное волнение может вызвать у Вас боль в желудке?',
    'Вы плохо переносите жаркую погоду?',
    'Зимой у Вас быстро замерзают руки?',
    'Ваша кожа чувствительна к солнцу?',
    'От усталости у вас болит голова?',
    'Вас напрягает холодная погода?',
    'Вы всегда понимаете человека на полуслове?',
    'Вы чувствуете, когда кто-то смотрит Вам в спину?',
    'Вы часто обжигаете язык, пробуя горячую еду?',
    'Вы боитесь щекотки?'
]


print('Заполните данные о себе. Пожалуйста, вводите достоверные данные, иначе программы запросит вас о повторном вводе')

sex = None
age = None
name = ''

print('Ваш пол: \n1. Мужской \n2. Женский')
while True:
    ans = input()
    if len(ans) == 0 or not ans.isdigit() or not validate_sex(int(ans)):
        print('Неверный ввод. Повторите заново')
        continue
    sex = SexEnum(int(ans))
    break

print('Введите ваш возраст: ')
while True:
    ans = input()
    if len(ans) == 0 or not ans.isnumeric() or not validate_age(int(ans)):
        print('Неверный ввод. Повторите заново')
        continue
    age = int(ans)
    break

print('Ввведите Вашу фамилию: ')
while True:
    ans = input()
    if len(ans) == 0 or not validate_name(ans):
        print('Неверный ввод. Повторите заново')
        continue
    name += ans + ' '
    break

print('Ввведите Ваше имя: ')
while True:
    ans = input()
    if len(ans) == 0 or not validate_name(ans):
        print('Неверный ввод. Повторите заново')
        continue
    name += ans + ' '
    break

print('Ввведите Ваше отчество: ')
while True:
    ans = input()
    if len(ans) == 0 or not validate_name(ans):
        print('Неверный ввод. Повторите заново')
        continue
    name += ans
    break

score = 0
print('Вам предлагается ответить на 12 вопросов. '
      'Вводите корректные данные, иначе программа попросит вас повторить ввод')
for question in questions:
    print(question)
    print('1. Да \n2. Нет')
    while True:
        ans = input()
        if len(ans) == 0 or not ans.isdigit() or not validate_sex(int(ans)):
            print('Неверный ввод. Повторите заново')
            continue
        if int(ans) == 1 or int(ans) == 2:
            score += int(ans) % 2
            break

print(f'Сумма полученных баллов: {score}')
print(f'Ваш уровень общей неспецифической реактивности организма: {get_reactivity_level(score)}')

session_date = str(datetime.now().date())

path = os.path.dirname(os.path.abspath(__file__))
path += f'\{name}'

# Если папки нет, то создаём
if not os.path.exists(path):
    os.makedirs(path)

with open(f'{path}\{session_date}.txt', 'w') as f:
    f.write(f'Время сеанса: {str(datetime.now())}\n')
    f.write(f'ФИО: {name}, возраст: {age} лет, пол: {get_age(sex)}\n')
    f.write(f'Сумма полученных баллов: {score}\n')
    f.write(f'Уровень общей неспецифической реактивности организма: {get_reactivity_level(score)}')

print(f'Результаты опроса сохранены в файл по пути {path}')
print("Нажмите Enter для продолжения...")
input()
