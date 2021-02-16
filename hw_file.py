# 1)Из текстового файла удалить все слова, содержащие от трех до пяти символов,
# но при этом из каждой строки должно быть удалено только четное количество таких слов.

# def delete_words(file_name):
#     """It takes an argument - the name of the file.
# Reads the file and writes the matching words to a new list, then overwrites from this list to the file.
# I haven't figured out how to remove an even number, but maybe I can't think of it = ("""
#     count_delete = 0
#     new_lis_word = []
#     with open(file_name, 'r', encoding='utf-8') as file:
#         for line in file:
#             words = line.split()
#             # print(words)
#             for word in words:
#                 word_without_punc = delete_punc(word)
#                 if len(word_without_punc) < 3 or len(word_without_punc) > 5:
#                     new_lis_word.append(word_without_punc)
#                     count_delete += 1
#                 # print(new_lis_word, 'new')
#     with open(file_name, 'w', encoding='utf-8') as file:
#         for word in new_lis_word:
#             file.write(word + ' ' + '\n')
#
# def delete_punc(word):
#     """Removes punctuation."""
#     from string import punctuation
#     for punc in punctuation:
#         if punc in word:
#             word = word.replace(punc, '')
#     return word
#
# delete_words('hw_file_1.txt')

# 2)Текстовый файл содержит записи о телефонах и их владельцах.
#     Переписать в другой файл телефоны тех владельцев, фамилии которых
# начинаются с букв К и С.

# def phone_number_selection(original_file, selected_file):
#     """The function takes two arguments. 1 - original file;
#     2 - the file into which we will write the selected data."""
#     with open(original_file, 'r', encoding='utf-8') as file:
#         for elem in file:
#             phone_lis = elem.split()
#             print(phone_lis)
#             for last_name in phone_lis:
#                 print(last_name)
#                 if last_name[0] == 'К' or last_name[0] == 'С':
#                     with open(selected_file, 'a', encoding='utf-8') as file_1:
#                         for elem in phone_lis:
#                             file_1.write(elem + ' ')
#                         file_1.write('\n')
#
#
# phone_number_selection('hw_file_2.txt', 'hw_file_2.2.txt')

# 3)Получить файл, в котором текст выровнен по правому
# краю путем равномерного добавления пробелов.

# def far_right_text()