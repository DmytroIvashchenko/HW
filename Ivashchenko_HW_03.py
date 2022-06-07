import re  # використовується в 5-му завданні.

#  №1. Программа, що запитує в користувача вік та згідно нього рекомендує країну для відвідування.
year_birthday = (input("Please, enter your year of birth "))
if year_birthday.isdigit() is False:
    print("Enter number")
    year_birthday = (input("Please, enter your year of birth "))
    if year_birthday.isdigit() is False:
        print("Error")
    elif int(year_birthday) == 21:
        print("You should visit Holland.")
    elif int(year_birthday) > 21:
        print("You should visit Vietnam.")
    else:
        print("Travel everywhere")

# №2. Програма, що питає в користувача ім'я, стать, вік, згідно цих даних рекомендує фільм для перегляду.
print("Hello user!")
name = input("Enter your name ")
gender = input("Indicate your gender: Male/Female")
age = int(input("Please, enter your age "))
if name == "Admin":
    print("Hello, Lord! ")
if name == "Eugene":
    print("I'd advise you to watch Tenet ")
elif 14 > age > 10 or age > 30 and gender == "Male":
    print("I'd advise you to watch StarWars or Mandalorean ")
elif 22 > age > 32 and gender == "Female":
    print("I'd advise you to watch Transformers ")
elif age < 16 and gender == "Female":
    print("I'd advise you to watch The Insurgent")
elif age < 11 and gender == "Male":
    print("I'd advise you to watch ", "TMNT", sep="\n")
if name == "Guido":
    print(end="Thank you very much. ")

# №3. Програма виводить на екран кожен 5-й елемент послідовності.
text = '(etnfづzxfk｡12dt◕`1ad‿6hns‿1zQY◕Cd$y｡FtSq)Ze6?づ#2)$'
text = text[0:50:5]
print(text)

#  №4. Програма переводу земних днів у марсіанські соли.
earth_time = list(map(int, input("Enter number_earth_days, Enter number_hours ").split()))  # день и часы вместе
maear = round(1.02595675 * (earth_time[0] + earth_time[1] / 24), 2)
print(f'Maear is {maear}')

#  №5. Програма, що замальовує слово черт на ####.

text_input = input("Введіть текст: ")
print(re.sub(r'(?i)черт(?=\W)', '####', text_input))
