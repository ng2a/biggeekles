# # 1 задание
def plus(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'На ноль делить нельзя'
print(plus(2, 0))
#
# # 2 задание
def data(name, surname, year, city, email, phone):
    print('{} {} {} {} {} {}'.format(name, surname, year, city, email, phone))
data('vanya', 'ivanov', '1990', 'Spb', 'Email', 'Phone')

# 3 задание
def my_func(arg1, arg2, arg3):
    a = [arg1, arg2, arg3]
    a.remove(min(arg1, arg2, arg3))
    return sum(a)
print(my_func(1, 2, 3))

# 4 задание
def my_func4(x, y):
    print(x ** y) # первый способ
    znam = x # второй способ
    for i in range(1, -y):
        znam = znam * x
    print(1 / znam)
my_func4(2, -2)

# 5 задание
def my_func5():
    result = 0
    while True:
        print('Введите числа через пробел или Q для выхода:')
        user_input = input().split(' ')
        numbers = list(filter(lambda x: x.isnumeric() == True, user_input))
        others = list(filter(lambda x: x.isnumeric() == False, user_input))
        numbers = list(map(lambda x: float(x), numbers))
        result+=sum(numbers)
        print("Сумма: ")
        print(result)
        if 'Q' in others:
            print('Пока!')
            break
my_func5()

# 6 задание
def int_fuck(string):
    if string:
        return string[0].upper() + string[1:]
    return string[:]

print(int_fuck('vanaysdkj asd'))







# Дальше идет код с лекций


# list1 = ['zz', 'aa', 'qwer']
# print(max(list1, key=len))
# print(round(1.837, 2))
# for i, val in enumerate(['a', 'b', 'c'], start=1):
#     print(i, val)
#
# def say_hello(a):
#     print('Hello', a)
# say_hello('Ivan')

# def average(numbres):
#     result = sum(numbres) / len(numbres)
#     return result
# out = average([1,2,3,4,5])
# print(out)

# def qwe(a):
#     pass
# print(qwe(500))
#
# x = 1
# def test():
#     x = 2
# test()
# print(x)
#
# x = 1
# y = 3
# def test(x):
#     x += 1
#     return x
#
# y = test(y)
# print(y)
#
# x = 1
# def test(x):
#     x += 1
#     return x
# x = test(x)
# print(x)
#
# def test(name='Name', surname='Guest'):
#     print(name, surname)
#
# test('Ivan', 'Ivanov')

# def test(name, val, *args):
#     print(name, val, args)
#
# test('Ivan', 'Ivanov', 1, 2, 3)
#
# def mfunc(name, age, surname):
#     print(name, surname, age)
#
# mfunc('Ivan', 'Ivanov', 50)
# mfunc(age=5, surname='Ivanov', name='Ivan')
#
# def myfunc(name, **kwards):
#     print(name, kwards)
#
# myfunc(age=5, name='ivan', surname='Ivanov')
#
# names = ['Igor', 'Ivan', 'Andrey']
# ages = [50, 15, 28]
#
# for name, age in zip(names, ages):
#     print(name, age)
# print(list(zip(names, ages)))
#
# def myfunc(x):
#     return x**2
#
# data = [-2, -1, 5, 20]
# result = []
# for i in data:
#     result.append((myfunc(i)))
# print(result)
#
# result = list(map(myfunc, data))
# print(result)
#
# result = list(filter(myfunc, data))
# print(result)

# result = list(map(lambda x: x**2, data))
# print(result)
#
#
# print(range(10))
# for i in range(5, 10, 2):
#     print(i)

# def mfunc (name, age, surname):
#     print(name, age, surname)
#     """"
#     :param name: its name
#     :param age: its age
#     :param surmane: its surname
#     """
# x = mfunc(name=1,age=2, surname=3)

