# Задача-1
# Создать объект менеджера контекста который будет переходить в
# папку которую он принимает на вход. Так же ваш объект должен принимать
# исключение которое он будет подавлять Если флаг об исключении
# отсутствует, исключение должно быть поднято.
import os

class OpenFolder:
    def __init__(self, path, *exception):
        self.path = path
        self.exception = exception
        """We save the current path so that we can close it later."""
        self.saved_cwd = os.getcwd()


    def __enter__(self):
        try:
            """Trying to take a new path."""
            os.chdir(self.path)
        except self.exception:
            print('Ooops, something went wrong')

        return self.path

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Closing the old path"""
        os.chdir(self.saved_cwd)

with OpenFolder(r'C:\Users', FileNotFoundError):
    print(os.getcwd())
