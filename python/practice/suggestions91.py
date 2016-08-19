
# assert a == b, 'not equal'

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# from itertools import islice
# print(list(islice(fib(), 5)))

# from ast import literal_eval
# a = literal_eval('5 + 6')
# print(a)

# a, b = 5, 6
# literal_eval('a, b = b, a')
# print(b)

# a = 'Hello {0}'.format('Howard')
# print(a)

a = [1, 2, 4, 6]
b = [i ** 2 if i % 2 == 0 else i + 1 for i in a]
print(b)