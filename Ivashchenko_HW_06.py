#  №1. Написати програму яка складає декілька словників в один.
first = {1: 10, 2: 20}
second = {3: 30, 4: 40}
third = {5: 50, 6: 60}
fourth = {7: 70, 8: 80}
fifth = {9: 90, 10: 100}
all_dict = first | second | third | fourth | fifth  # більш короткий спосіб
print(all_dict)

all_dict.clear()  # більш довгий способ
all_dict = first.copy()
all_dict.update(second)
all_dict.update(third)
all_dict.update(fourth)
all_dict.update(fifth)
print(all_dict)

#  №2. Написати програму в якій створити словник із ключами від 11 до 20 включно.
#      Значення = квадрати ключі. Скласти всі значення (values) в один рядок та відсортувати словник за ключами.
dict_number = {i: i ** 2 for i in range(11, 20, 1)}
print(dict_number)
print(sum(dict_number.values()))
list_keys = list(dict_number.keys())
list_keys.sort(reverse=True)
dict_number = {i: i ** 2 for i in list_keys}
print(dict_number)

#  №4. Написати програму, яка видаляє дублікати з dictionary.
all_pupils = {'id1': {'name': 'Ruslan', 'class': 1, 'subjects': {'Math', 'Algorithms', 'English'}}, \
              'id2': {'name': 'Mark', 'class': 2, 'subjects': {'Geometry', 'Java', 'Cooking'}}, \
              'id3': {'name': 'Ruslan', 'class': 1, 'subjects': {'Math', 'Algorithms', 'English'}}}
print(all_pupils)
#  перший спосіб, через цикл for
new_d = {}
for k, v in all_pupils.items():
    if v not in new_d.values():
        new_d.update({k: v})
print(new_d)

# другий спосіб, через dict-comprehension
res = {}
[res.update({k: v}) for k, v in all_pupils.items() if v not in res.values()]
print(res)

#  №5. Написати програму яка повертає з dictionary всі унікальні values.
#  Доповнення: Повернути ту саму структуру.

list1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
print(f'Raw data: {list1}')
# s = set(val for dic in list1 for val in dic.values())
# print(s) #  все уникальные значения можно вернуть через set, но для выполнения задания c усложнением нужен список
list_val = list(val for dic in list1 for val in dic.values())
print(f'All values: {list_val}')
list2 = []
for item in list_val:
    if item not in list2:
        list2.append(item)
print(f'Unique values: {list2}')
new_list_of_dict = []
for dic in list1:
    for k, v in dic.items():
        for i in list2:
            if v in list2:
                list2.remove(v)
                new_list_of_dict.append(dic)
print(
    f'Dictionary L: {new_list_of_dict}')  # [{"V":"S001"}, {"V": "S002"}, {"VI": "S005"}, {"V":"S009"},{"VIII":"S007"}]

#  №6 Написати програму,яка порахує загальну кількість найменувань у списку. Лише у списках!
schedule = {'monday': ['clean house', 'drive car', 'meet with freands'], 'thuesday': None,
            'wednesday': ['manicure', 'hammam', 'beer']}
list_of_items = []
for key, value in schedule.items():
    if type(value) == list:
        list_of_items.extend(value)
print(f'Result: {len(list_of_items)}')
