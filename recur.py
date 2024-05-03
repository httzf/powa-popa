def F3(a, g):
    if a > g:
        return 0
    if a == g:
        return 1
    else:
        return F3(a + 2, g) + F3(a + 4, g)
print (F3(4, 22))



def F9(a1, g1):
    if a1 > g1:
        return 0
    if a1 == g1:
        return 1
    else:
        return F9(a1 + 1, g1) + F9(a1 * 2, g1) + F9(a1 * 3, g1)
print(F9(1, 13))

def f1(a, b):
    if a == b:
        return 1
    if a > b:
        return 0
    else:
        return f1(a + 1, b) + f1(a * 2, b) + f1(a + 3, b)

print(1, f1(3, 12) * f1(12, 16))


def f2(a, b):
    if a == b:
        return 1
    if a > b or a == 17:
        return 0
    else:
        return f2(a + 1, b) + f2(a + 2, b) + f2(a * 3, b)


print(f2(3, 10) * f2(10, 25))




# def f4(a, b):
#     if a == b:
#         return 1
#     if a > b:
#         return 0
#     else:
#         return f4(a - 1, b) + f4(a + 3, b) + f4(a * 2, b)
#
# print(f4(3, 10) * f4(10, 25))
# pass



def F5(a, g):
    if a > g:
        return 0
    if a == g:
        return 1
    else:
        return F5(a + 1, g) + F5(a * 4, g)
print(F5(1, 29))








