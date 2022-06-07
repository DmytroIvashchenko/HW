#  №1. Написати програму в якій користувач вводить пароль вперше система запам'ятовує і просить повторити пароль
#      Перевіряє його якщо ні, то просить повторити.
#      А якщо збігся то повідомлення.
password_one = input('Enter password ')
password_two = input('Enter again password ')
while password_two == password_one:
    print('Password is True, thank you for registration')
    if password_one != password_two:
        password_two = input('Error, incorrect password. Enter again password ')
    break

#  №2. Написати програму в якій даний список з значеннями, що повторюються.
#      Необхідно з нього видалити всі певні значення ('eg') використовуючи while цикл.
product = ['bear', 'milk', 'eg', 'eg', 'eg', 'eg']
print(f'{product}')
i = len(product) - 1
while 0 < i <= len(product):
    if product[i] == 'eg':
        del product[i]
    i -= 1
print(f'{product}')

#  №3. Написати програму в якій дан список довільний з int
#      потрібно вивести "all numbers are even" якщо всі парні та NO якщо ні.
numbers = [int(number) for number in input('Enter numbers, separate the numbers with commas ').split(',')]
i = len(numbers) - 1
a = 0
while 0 <= i <= len(numbers):
    if (numbers[i] % 2) != 0:
        a += 1
        i -= 1
        continue
    else:
        i -= 1

if a == len(numbers):
    print('All numbers are even')
else:
    print('No')

# №4. Написати програму яка буде створювати список методів з доступних (стандартних) методів пітон об'єктів.
object_python = input('Enter object ')
if object_python == 'set':
    list_method = dir(set)
elif object_python != 'set':
    if object_python == 'int':
        list_method = dir(int)
    if object_python == 'dict':
        list_method = dir(dict)
    if object_python == 'list':
        list_method = dir(list)
    if object_python == 'tuple':
        list_method = dir(tuple)

if object_python == 'str':
    list_method = dir(str)
i = len(list_method) - 1
while 0 <= i <= len(list_method):
    list_method[i].split()
    if '__' in list_method[i]:
        del list_method[i]
        i -= 1
    else:
        print(f'{list_method[i]}')
        i -= 1

#  №6. Написати приклади всіх методів із set об'єкта.
set1 = {1, 2, 3}
print(set1)
set1.add(4)  # add
print(set1)
set1.update([2, 3, 4, 5])  # update
print(set1)
set1.remove(4)  # delete element, If it was not there, there is an error
print(set1)
set1.discard(5)  # delete element . If it was not there, the error does not occur
print(set1)
set1.pop()  # Removes an arbitrary element and returns it.
print(set1)
set1.clear()  # Deletes all elements of the set
print(set1)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set2.intersection(set1, set2)
print(set2)
set2.difference(set1, set2)
print(set2)
set2.isdisjoint(set1)
print(set2, set1)
set1.issubset(set2)
print(set1, set2)
set2.issuperset(set1)
print(set1, set2)
set3 = {8, 9}
set3.union(set1, set2)
print(set3)
