from typing import Union
from datetime import datetime
from sympy import sympify
import time


class Calculator:
    def timer(delay_seconds): # Декоратор с аргументом на задержку в секундах
        def wrapper(func):
            def inner(*args, **kwargs):
                start_time = datetime.now()
                result = func(*args, **kwargs)
                time.sleep(delay_seconds)
                end_time = datetime.now()
                print(f'Пауза в решении: {delay_seconds} секунды. Общее время вычисления заняло с учётом задержки: {(end_time - start_time)}')
            return inner
        return wrapper

    @timer(3)
    def calculation(value_1:Union[int, float], value_2:Union[int, float], operation:str) -> str:
        lst = {'+':'Сложения', '-':'Вычитания', '*':'Умножения', '/':'Деления', '//':'Целочисленного деления', '%':'Остаток от деления', '**':'Возведения в степень'}
        for key, value in lst.items():
            if operation == key or operation == value:
                print(f'Результатом операции {value}, является', sympify(f'{value_1} {operation} {value_2}'))


Calculator.calculation(input('Введите первое значение: '), input('Введите второе значение: '), input('Введите операцию вычисления: '))





