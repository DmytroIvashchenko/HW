#  №1. Написати программу котра буде запитувати у юзера імʼя та вік.
#      Після видавати певну інформацію згідно отриманної відповіді
def registration():
    name_man = input("What is you name_man?")
    age = int(input("How old are you?"))
    if 70 > age > 16:
        print(f'Welcome {name_man}, on your website')
    elif age == 16:
        print(f'Dear {name_man} need to wait one year')
    elif 90 >= age >= 70:
        print(f'You are lucky, {name_man} and welcome.')
    elif 121 >= age > 90:
        print(f'Not described in the task, Ruslan:)')
    elif age > 121:
        print(f'You are not real, {name_man}')
    else:
        print(f'Im sorry, {name_man}, you are too young.')
    yes = input("Do you want a registration new member? Yes/No ")
    if yes == 'Yes':
        registration()
    elif yes == 'No':
        print(f'Bye, {name_man}.')
    else:
        print('Error')


registration()

# №2. У файлі створити приклади використання якомога більшої кількості операторів.
budget = int(input('Enter your budget'))
print("Now let's find out how many cookies you can buy")
name = input('Choose an ingredient ')
if name == 'Flour':
    flour = int(input('Product price per kilo '))
    flour_per_one = (flour / 1000) * 20
    name = input('Thank you, please choose next ingredient or Do you have all the ingredients written down? ')
if name == 'Cocoa':
    cocoa = int(input('Product price per kilo '))
    cocoa_per_one = (cocoa / 1000) * 2.5
    name = input('Thank you, please choose next ingredient or Do you have all the ingredients written down?')
if name == 'Sugar':
    sugar = int(input('Product price per kilo '))
    sugar_per_one = (sugar / 1000) * 10
    name = input('Thank you, please choose next ingredient or Do you have all the ingredients written down? ')
if name == 'All':
    cookie = flour_per_one + cocoa_per_one + sugar_per_one
    print(f'Cookies price is {cookie}')
cookies_Quantity = int(input('How many cookies you buy?'))
purchase_Sum = cookie * cookies_Quantity
change = budget - purchase_Sum
if change > 0:
    print(f'You just bought {cookies_Quantity} cookie,your spend {purchase_Sum} UAH, you change is {change} UAH')
else:
    print('Not enough money')
