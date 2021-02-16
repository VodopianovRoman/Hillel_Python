# Задача-1
# У вас есть список(list) IP адрессов. Вам необходимо создать
# класс который будет иметь методы:
# 1) Получить список IP адресов
# 2) Получить список IP адресов в развернутом виде
# (10.11.12.13 -> 13.12.11.10)
# 3) Получить список IP адресов без первых октетов
# (10.11.12.13 -> 11.12.13)
# 4) Получить список последних октетов IP адресов
# (10.11.12.13 -> 13)
#

# class IpAdres:
#     lis_ip = ['06.07.08.09', '10.11.12.13', '14.15.16.17']
#
#     def __init__(self, lis_ip):
#         self.l_ip = lis_ip
#
#     def get_ip(self,l_ip):
#         return self.l_ip

lis_ip = ['06.07.08.09', '10.11.12.13', '14.15.16.17']

# def reverse_ip(primordial_lis):
#     reverse_lis_start = []
#     reverse_lis_end = []
#     for ip in primordial_lis:
#         reverse_lis_start = ip.split('.')
#         reverse_lis_start = reverse_lis_start[::-1]
#         reverse_lis_end.append('.'.join(reverse_lis_start))
#
#     return reverse_lis_end
# reverse_ip(lis_ip)

# def non_first_oktet(primordial_lis):
#     reverse_lis_start = []
#     reverse_lis_end = []
#     for ip in primordial_lis:
#         reverse_lis_start = ip.split('.')
#         reverse_lis_start = reverse_lis_start[1:]
#         reverse_lis_end.append('.'.join(reverse_lis_start))
#     print(reverse_lis_end)
# non_first_oktet(lis_ip)

# def last_oktet(primordial_lis):
#     reverse_lis_start = []
#     reverse_lis_end = []
#     for ip in primordial_lis:
#         reverse_lis_start = ip.split('.')
#         reverse_lis_start = reverse_lis_start[-1:]
#         reverse_lis_end.append('.'.join(reverse_lis_start))
#     print(reverse_lis_end)
# last_oktet(lis_ip)

# Задача-2
# У вас несколько JSON файлов. В каждом из этих файлов есть
# произвольная структура данных. Вам необходимо написать
# класс который будет описывать работу с этими файлами, а
# именно:
# 1) Запись в файл
# 2) Чтение из файла
# 3) Объединение данных из файлов в новый файл
# 4) Получить путь относительный путь к файлу
# 5) Получить абсолютный путь к файлу
#
import json
import pprint
# some_data = [{'a': 1, 'b': 2},{'c': 3, 'd': 4},{'e': 5, 'f': 6}]
# def write_json(name_json):
#     with open(name_json, 'w') as json_file:
#         json.dump(some_data, json_file, indent=2)
# write_json('example_json_result.json')
#
# def read_json(name_json):
#     with open(name_json) as json_file:
#         data = json.load(json_file)
#         pprint.pprint(data)
#
#
# def union_json_files(first_name_json, second_name_json, write_name_json):
#     with open(first_name_json) as first_json_file:
#         data_first = json.load(first_json_file)
#
#     with open(second_name_json) as second_json_file:
#         data_second = json.load(second_json_file)

    # data_second.update(data_first)
    # """If you need to combine with key update."""
    # with open(write_name_json, 'w') as write_json_file:
    #     json.dump(data_second, write_json_file, indent=2)

    # """If it is necessary to add"""
    # with open(write_name_json, 'a') as write_json_file:
    #     json.dump(data_first, write_json_file, indent=2)
    #     json.dump(data_second, write_json_file, indent=2)


# union_json_files('example_json_1.json', 'example_json_2.json', 'example_json_result.json')

# Задача-3
#
# Создайте класс который будет хранить параметры для
# подключения к физическому юниту(например switch). В своем
# списке атрибутов он должен иметь минимальный набор
# (unit_name, mac_address, ip_address, login, password).
# Вы должны описать каждый из этих атрибутов в виде гетеров и
# сеттеров(@property). У вас должна быть возможность
# получения и назначения этих атрибутов в классе.


