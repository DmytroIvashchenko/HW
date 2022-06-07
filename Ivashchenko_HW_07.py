from math import sqrt


# Написати функцію яка як аргумент приймає розмір сторони квадрата, а повертає кортеж у якому лежать три значення:#
# периметр квадрата, діагональ квадрата, площа квадрата

def square(side_of_square):
    if side_of_square > 0:
        area_of_square = side_of_square * side_of_square
        perimetr_square = side_of_square * 4
        diagonal_square = sqrt(2) * side_of_square
        result = area_of_square, perimetr_square, diagonal_square
        return result
    else:
        print("Incorrect number")


user_square = square(int(input("Please enter side of square ")))
print(user_square)


# №2.Написати функцію яка приймає як аргумент номер місяця, повертає рядок - пору року, цього місяця
def season(number_of_month):
    if number_of_month == 1 or number_of_month == 2 or number_of_month == 12:
        return 'It is a winter month'
    elif number_of_month == 3 or number_of_month == 4 or number_of_month == 5:
        return 'It is a spring month'
    elif number_of_month == 6 or number_of_month == 7 or number_of_month == 8:
        return 'It is a summer month'
    elif number_of_month == 9 or number_of_month == 10 or number_of_month == 11:
        return 'It is a autumn month'
    else:
        return 'Incorrect number'


your_season = season(int(input("Enter number of month 1 to 12 ")))
print(your_season)

# №3. Написати функцію, яка приймає як аргументи два списки, а повертає список,
# що складається з елементів цих двох списків, причому перший елемент списку - перший елемент першого аргументу,
# другий елемент списку - перший елемент другого списку, третій елемент - другий елемент першого списку,
# четвертий – другий елемент другого аргументу тощо.
a = [1, 2, 3]
b = [11, 22, 33]


def sort_number(*args):
    c = []
    n = 0
    while n != len(a):
        c.append(a[n])
        c.append(b[n])
        n += 1


list_member = sort_number(a, b)
print(list_member)


# №4. Написати функцію яка приймає як аргумент рядок, і повертає True, якщо рядок є поліндромом і False якщо ні.

def is_palindrome(word):
    return word == word[::-1]


palindrome = is_palindrome(input('Enter text '))
print(palindrome)
