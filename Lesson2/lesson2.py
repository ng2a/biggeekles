# 1 задача
a_list = [20, "Привет", 2.5]
i = len(a_list)
while i > 0:
    i -= 1
    print(type(a_list[i]))
else:
    print("Проверка типа каждого элемента пройдена")

# 2 задача
print("Введите количество элементов списка: ")
n = int(input())

print("Введите элементы списка: ")
b_list = []
for i in range(n):
    b_list.append(int(input()))

o = len(b_list)
m = 0
n = 1
if o % 2 == 0:

    while o > 0:
        o -= 2
        b_list[m], b_list[n] = b_list[n], b_list[m]
        m += 2
        n += 2
    else:
        print(b_list)
else:
    while o > 1:
        o -= 2
        b_list[m], b_list[n] = b_list[n], b_list[m]
        m += 2
        n += 2
    else:
        print(b_list)

# 3 задача
month = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август', 9: 'Сентябрь',
         10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
print("Введите число от 1 до 12")
month_user = int(input())

if 0 < month_user < 13:
    print(month.get(month_user))
    if 2 < month_user < 6:
        print("Это весенний месяц")
    elif 5 < month_user < 9:
        print("Это летний месяц")
    elif 8 < month_user < 12:
        print("Это осенний месяц")
    else:
        print("Это зимний месяц")
else:
    print("Такого месяца не существует")

# через list ПОКА НЕ РАБОТАЕТ

winter_list = [1, 2, 12]
spring_list = [3, 4, 5]
summer_list = [6, 7, 8]
autumn_list = [9, 10, 11]
n = int(input())


def check(winter_list, spring_list, summer_list, autumn_list):
    if n in winter_list:
        time = 'winter'
    elif n in spring_list:
        time = 'spring'
    elif n in summer_list:
        time = 'summer'
    else:
        time = 'autumn'
    return time

# 4 задача

