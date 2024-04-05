
def fact(x):
    if x <= 1:
        return 1
    else:
        return x*fact(x-1)


def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n-2) + (n+1)


def matryoshka(m):
    if m == 0:
        print('маленькая матрешечка 0')
    elif m > 0:
        print(f'верх матрешки {m}')
        matryoshka(m-1)
        print(f'низ матрешки {m}')


def gdc(a, b):
    if a == b:
        return a
    elif a > b:
        return gdc(a-b, b)
    elif a < b:
        return gdc(a, b-a)


def pow1(a, n):
    print(a, n)
    if n == 0:
        return 1
    return a * pow1(a, n - 1)

def pow2(a, n):
    print(a, n)
    if n == 0:
        return 1
    if n % 2 == 0:
        return pow2(a*a, n // 2)
    else:
        return a*pow2(a, n - 1)




print(pow2(139268, 3420510))



#matryoshka(5)

