# Задача-1
# Создать объект менеджера контекста который будет переходить в
# папку которую он принимает на вход. Так же ваш объект должен принимать
# исключение которое он будет подавлять Если флаг об исключении
# отсутствует, исключение должно быть поднято.
import os
import contextlib
import time
from contextlib import suppress

class OpenFolder:
    def __init__(self, path, *exception):
        self.path = path
        self.exception = exception
        """We save the current path so that we can close it later."""
        self.saved_cwd = os.getcwd()

    def __enter__(self):
        try:
            """To test 3 tasks"""
            time.sleep(5)
            """Trying to take a new path."""
            os.chdir(self.path)
        except self.exception:
            print('Ooops, something went wrong')

        return self.path

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Closing the old path"""
        os.chdir(self.saved_cwd)
#
# with OpenFolder(r'C:\Users', FileNotFoundError):
#     print(os.getcwd())

# Задача -2
# Описать задачу выше но уже с использованием @contexmanager

@contextlib.contextmanager
def open_folder(path, *exception):
    now_cwd = os.getcwd()
    try:
        os.chdir(path)
        yield
    except exception:
        print('Ooops, something went wrong')
        os.chdir(now_cwd)
    finally:
        os.chdir(path)

with suppress(FileNotFoundError):
    with open_folder(r'C:\Users', FileNotFoundError) as op_fol:
        op_fol =os.getcwd()
        print(op_fol)

# Задача -3
# Создать менеджер контекста который будет подсчитывать время выполнения вашей функции

class CountOfFunc:
    def __init__(self, ):
        self.time_start = time.time()
        # self.context_manager = context_manager
        # self.exception = exception

    def __enter__(self):
        try:
            # self.context_manager
            self.time_start
            # time.sleep(15)
        except Exception:
            print('Ooops, something went wrong')

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # self.context_manager
        self.time_stop = time.time()
        print(f'Time spent on the function: {self.time_stop-self.time_start}')


# with CountOfFunc():
#     with OpenFolder(r'C:\Users',FileNotFoundError):
#         print(os.getcwd())