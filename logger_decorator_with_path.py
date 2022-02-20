from datetime import datetime
import pathlib
from pathlib import Path

path = Path(pathlib.Path.home(), 'Decorators', 'logger_decorator.txt')

def logger_decorator_with_path(file_path):

    def logger_decorator(old_function):

        def new_function(*args, **kwargs):
            date_and_time = datetime.now()
            function_name = old_function.__name__
            result = old_function(*args, **kwargs)
            with open('logger_decorator.txt', 'a', encoding='UTF-8') as f:
                f.write(f'Дата и время вызова функции: {date_and_time}\n'
                        f'Имя функции: {function_name}\n'
                        f'Аргументы: {args, kwargs}\n'
                        f'Результат: {result}\n')
            return result
        return new_function
    return logger_decorator


if __name__ == '__main__':

    @logger_decorator_with_path(path)
    def summ(a, b):
        return a+b

    summ(3, 7)
