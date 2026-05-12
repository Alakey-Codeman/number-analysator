try:
    num = int(input('Введите число: '))
except ValueError:
    quit()

def square(x):
    print(x*x)
    return x*x


def cube(x):
    print(x*x*x)
    return x*x*x


def even(x):
    if x % 2 == 0:
        print('Чётное')
        return
    else:
        print('Нечётное')
        return

def posit(x):
    if x > 0:
        print('Положительное')
        return
    else: print('Отрицательное')
    return

def del3(x):
    if x%3 == 0:
        print('Делится на 3')
        return
    else: print('Не делится на 3')
    return

def del5(x):
    if x%5 == 0:
        print('Делится на 5')
        return
    else: print('Не делится на 5')
    return

def analyze(x):
    square(x)
    cube(x)
    even(x)
    posit(x)
    del3(x)
    del5(x)
    return
x = analyze(num)