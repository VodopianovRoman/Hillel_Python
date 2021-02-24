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
    """This context manager takes the path to the folder and the name of the error.
    In the __init__ block, we save our current file location.
    The folder is opened in the __enter__ blocks, here the error is suppressed using the construction
try except, if an error occurs, we enter the message and remain at the current location.
    In the __exit__ block, the saved location is closed."""

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
            os.chdir(self.saved_cwd)

        return self.path

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Closing the old path"""
        os.chdir(self.saved_cwd)
#
# with OpenFolder(r'C:\asd', FileNotFoundError):
#     print(os.getcwd())

# Задача -2
# Описать задачу выше но уже с использованием @contexmanager

@contextlib.contextmanager
def open_folder(path, *exception):
    """With the help of this decorator of the context manager, we get the path to the folder and
    go to it using the construction try/except.
        We keep our current location.
        In the final implementation, when invoked using visas, we use the suppres tool
    from the contextLib.
        Since without it, when specifying a non-existent path, the yield is swearing."""
    now_cwd = os.getcwd()
    try:
        os.chdir(path)
        yield
    except exception:
        os.chdir(now_cwd)
        print('Ooops, something went wrong')
    finally:
        os.chdir(path)

# with suppress(FileNotFoundError):
#     with open_folder(r'C:\asd', FileNotFoundError):
#         print(os.getcwd())

# Задача -3
# Создать менеджер контекста который будет подсчитывать время выполнения вашей функции

class CountOfFunc:
    """With the help of this context manager, we can calculate the execution time of the
    required function or context manager.
        In the variable time.start, we will remember the current time.
        In the __enter__ block, in try we start the countdown.
        In the __exit__ block, we display the time that was spent."""
    def __init__(self):
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