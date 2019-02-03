import random
count_fool = 0
game = 1
value = random.randint(1, 100)
print('Задуманное число = ' + str(value))
user = input('Введите число от 1 до 100  ')
check = user.isdigit()
while check != True and count_fool < 10:
    print('Вы не ввели число')
    user = input('Введите число от 1 до 100  ')
    count_fool += 1
    check = user.isdigit()
if check != True and count_fool == 10:
    print('\n' + 'Жаль, Вы не хотите играть =)')
if check == True and count_fool < 10:
        user = int(user)
        while user != value:
            if user < value:
             print('Введите число больше введенного')
             user = int(input('Введите число '))
             game += 1
            elif user > value:
             print('Введите число меньше введенного')
             user = int(input('Введите число '))
             game += 1
            if user == value:
                 print('Вы угадали загаданное число!' + '\n'+ 'Совершено для этого попыток: ' + str(game))