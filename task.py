# 1 -  Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*.
# приоритет операций стандартный. Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций. Пример: 1+2*3 => 7; (1+2)*3 => 9;
'''
from posixpath import split


OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
             '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}

def parse(formula_string):
        number = ''
        for s in formula_string:
            if s in '1234567890.': # если символ - цифра, то собираем число
                number += s  
            elif number: # если символ не цифра, то выдаём собранное число и начинаем собирать заново
                yield float(number) 
                number = ''
            if s in OPERATORS or s in "()": # если символ - оператор или скобка, то выдаём как есть
                yield s 
        if number:  # если в конце строки есть число, выдаём его
            yield float(number)  
            print(number)

formula_string ='2+2'
print(list(parse(formula_string)))
# Что делать дальше я не могу додуматься и так неделя ушла на эту задачу и я жестко отстал от группы
'''


# 2 - Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. Входные и выходные данные хранятся
# в отдельных файлах (в одном файлике отрывок из какой-то книги, а втором файлике — сжатая версия этого текста).
'''
import controll

def main():
    controll.compression()
main()
'''
# 3 -  ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, которая идет через 13 букв после нее в алфавите.
# ROT13 является примером шифра Цезаря.
# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13 .
# Если в строку включены числа или специальные символы, они должны быть возвращены как есть. Также создайте функцию,
# которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений).
# Не использовать функцию encode.
'''
alphabet = 'abcdefghijklmnopqrstuvwxyz'


def encoding(text, key):
    result = ''
    for i in text.lower():
        if i in alphabet:
            result += alphabet[(alphabet.find(i)+key) % len(alphabet)]
        else:
            result += i
    return result


def dencoding(text, key):
    result = ''
    for i in text.lower():
        if i in alphabet:
            result += alphabet[(alphabet.find(i)-key) % len(alphabet)]
        else:
            result += i
    return result


text = 'I will not give up, no matter how many years it takes!'
key = 13
encode_text= encoding(text,key)
print(f'Закодированный текст: {encode_text}')
decode_text = dencoding(encode_text, key)
print(f'Расшифрованный текст: {decode_text}')
'''