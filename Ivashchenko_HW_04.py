from collections import Counter  # Використовується у 2-му завданні.

#  №1. Написати програму, яка складатиметься з перших двох та останніх символів даного рядка
#  Якщо довжина рядку меньше 2 символів друкувати рядок типу, Ваш рядок занадто короткий.
text = input("Enter text ")
if len(text) < 2:
    print(f'Your string is too short - {text} ')
else:
    res_text = text[:2] + text[len(text) - 2:]
    print(f'{res_text}')

#  №2. Написати програму, яка підраховує кількість символів у рядку
#  і формує dict у якому key = буква, value = кількість їх у слові:
text_counter = list(input('Enter text '))
print(f'{len(text_counter)} symbol', Counter(text_counter), sep='\n')

#  №3. Програма приймає список продуктів та принтить найдовше слово та його довжину.
#  Використовувати ''.format() для виведення рядка та аргументів.
product = input('Enter product ').split()
product.sort(key=len, reverse=True)
print('The longest product name {}, {} symbols'.format(product[0], len(product[0])))

#  №4. Програма в якій користувач водить своє ім'я, програма повертає це ім'я в ВЕЛИКОМУ та маленькому регістрі.
text_correct = input('Enter text ')
print('{} {}'.format(text_correct.upper(), text_correct.lower()))

#  №5. Програма повертає унікальні слова відсортовані за абеткою.
text_unique = (list(set(input('Enter the text ').replace(',', '').split())))
text_unique.sort()
print(text_unique)

#  №6. Тема Кортеж та робота з ним.
#      Видалити елемент з кортежу.
tuple_one = 1, 2, 3
list_one = list(tuple_one)
list_one.pop()
tuple_two = tuple(list_one)
print(f'{tuple_one} is tuple_one;', type(tuple_one), '\n' f'{tuple_two} is tuple_two;', type(tuple_two))

#  №7. Написати програму яка цей список кортежів переведе до списку списків
tuple_correct = (1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)
print(type(tuple_correct), tuple_correct)
list_of_tuple = [list(x) for x in tuple_correct]
print(type(list_of_tuple), list_of_tuple)

# №8. Написати програму вихідними даними якої є послідовність чисел (-99, 99, 3)
#     У відповіді вивести чи ділиться число послідовності на 3 без остачі.
range_one = tuple(range(-99, 99, 3))
print(range)
for x in range_one:
    if x % 3:
        continue
    print(f'{x} ділиться без остачі на 3')

#  №9. Написати програму в якій дані два списки елементів якщо хоч один елемент збігається відпринт True.
list_1 = [13, 24, 35, 4, 5, 6, 9]
list_2 = [1, 3, 2, 456, 7, 12, 8, 9]
list_3 = []
for i in list_1:
    for j in list_2:
        if i == j:
            list_3.append(i)
            break
if list_3 != []:
    print(f'{list_3}')
else:
    print('У першому списку немає елементів з другого')
