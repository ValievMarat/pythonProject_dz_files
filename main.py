import pprint
import os

def get_cook_book_from_file(filename):
    dict = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            cook_name = line.strip()
            count_ingrids = int(file.readline())
            recept_list = []
            for index in range(count_ingrids):
                ingrids_dict = {}
                str = file.readline().strip()
                column_list = str.split('|')
                ingrids_dict['ingredient_name'] = column_list[0].strip()
                ingrids_dict['quantity'] = int(column_list[1].strip())
                ingrids_dict['measure'] = column_list[2].strip()
                recept_list += [ingrids_dict]
            file.readline()
            dict[cook_name] = recept_list
    return dict


def get_shop_list_by_dishes(dishes, person_count):
    dict_cooks = get_cook_book_from_file('recipes.txt')
    dict = {}

    #для контроля уникальности блюд, преобразуем список в множество
    set_dishes = set(dishes)
    for dish in set_dishes:
        ingrids_list = dict_cooks.get(dish)
        if not ingrids_list is None:
            for ingrid in ingrids_list:
                ingrid_name = ingrid['ingredient_name']
                list_ingrid = dict.get(ingrid_name)
                if list_ingrid is None:
                    dict[ingrid_name] = {'measure': ingrid['measure'], 'quantity': ingrid['quantity'] * person_count}
                else:
                    dict[ingrid_name]['quantity'] += ingrid['quantity'] * person_count

    return dict


def union_files(folder_name, file_list, result_name):
    current_dir = os.getcwd()
    folder_dir = os.path.join(current_dir, folder_name)

    list_info_files = []
    # Собираем в list_info_files общую информацию по всем файлам: список словарей dict_file
    for current_filename in file_list:
        dict_file = {}
        list_strings = []
        with open(os.path.join(folder_dir, current_filename), 'r', encoding='utf-8') as file:
            for line in file:
                list_strings += [line]
        dict_file['name'] = current_filename
        dict_file['length'] = len(list_strings)
        dict_file['strings'] = list_strings

        list_info_files.append(dict_file)

    # сортировка по количеству строк в файле list_info_files
    list_info_files = sorted(list_info_files, key = lambda x: x['length'])
    print(list_info_files)

    # создание итогового файла
    with open(result_name, 'w', encoding='utf-8') as file:
        for dict_file in list_info_files:
            file.write(f'{dict_file["name"]}\n')
            file.write(f'{str(dict_file["length"])}\n')

            for string_file in dict_file['strings']:
                file.write(string_file)

            file.write('\n')




# Задача 1
dict = get_cook_book_from_file('recipes.txt')
pprint.pprint(dict)
print()

# Задача 2
dict = get_shop_list_by_dishes(['Омлет', 'Омлет'], 2)
dict = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint.pprint(dict)
print()

# Задача 3
file_list = ['1.txt', '2.txt', '3.txt']
union_files('sorted', file_list, 'result.txt')