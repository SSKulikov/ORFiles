print('Задача №1')

cook_book = {}
with open('kafe.txt', 'r', encoding='utf-8') as f:
    for line in f:
        dish_name = line.strip()
        count = int(f.readline())
        ing_list = list()
        for item in range(count):
            ingrs = {}
            ingr = f.readline().strip()
            ingrs['ingredient_name'], ingrs['quantity'], ingrs['measure'] = ingr.split('|')
            ingrs['quantity'] = int(ingrs['quantity'])
            ing_list.append(ingrs)
        f.readline()
        cook_book[dish_name] = ing_list
print(cook_book)
print('')

print('Задача №2')
def get_shop_list_by_dishes(dishes, person_count):
    dict_1 = {}
    for dish, ingred in cook_book.items():
        if dish in dishes:
            for i in ingred:
                a = i.get('ingredient_name')
                i.pop('ingredient_name')
                if a not in dict_1.keys():
                    dict_1[a] = i
                    i['quantity'] *= person_count
                else:
                    dict_1[a]['quantity'] += i['quantity']
    print(dict_1)
    return

get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2)

print('')

print('Задача №3')

with open('folder/1.txt', 'r', encoding='utf-8') as file1, \
     open('folder/2.txt', 'r', encoding='utf-8') as file2,\
     open('folder/3.txt', 'r', encoding='utf-8') as file3,\
     open('folder/result.txt', 'a+', encoding='utf-8') as file_result:
    def lines_file(file_):
        line_file = file_.readlines()
        file_info = ['\n' + file_.name + '\n', str(len(line_file)) + '\n']
        return file_info + line_file

    list_files = [lines_file(file1), lines_file(file2), lines_file(file3)]
    r = sorted(list_files, key=len)
    result_text = r[0] + r[1] + r[2]
    for line in result_text:
        file_result.write(line)