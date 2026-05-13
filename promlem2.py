try:
    num = int(input('Введите число: '))
except ValueError:
    quit()

def square(x):
    print('Квадрат: ',x*x)
    return x*x


def cube(x):
    print('Куб: ',x*x*x)
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

def deln(x):
    n = 3
    while n < x:
        if x%n == 0:
            print('Делится на ',n)
        n += 1
    zap = 1
    n = 2
    while n < x:
        if x%n == 0:
            zap+=1
        if zap == 1:
            print('Простое число!')
            return
        return


def analyze(x):
    square(x)
    cube(x)
    even(x)
    posit(x)
    deln(x)
    return
x = analyze(num)