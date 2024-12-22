first = int(input('Введите первое целое цисло: '))
second = int(input('Введите второе целое цисло: '))
third = int(input('Введите третье целое цисло: '))
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
