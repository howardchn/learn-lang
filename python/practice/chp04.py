# alphabet = 'abcdefg' +\
#     'hijklmn' +\
#     'opqrst' +\
#     'uvwxyz'

# print (alphabet)

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['Banana', 'Orange', 'Peach']
desserts = ['Coffee', 'Tea', 'Beer']

# for day, fruit, dessert in zip(days, fruits, desserts):
#     data = {'day':day, 'fruit':fruit, 'dessert':dessert}
#     print ('day: %(day)s, fruit: %(fruit)s, dessert:%(dessert)s' % data)

numbers = [number for number in range(1, 10) if number % 2 == 0]
# print(numbers)

rows = range(1, 4)
cols = range(1, 3)

cells = [(row, col) for row in rows for col in cols]
# print(cells)

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
# print(letter_counts)

aset = (i for i in range(1, 6) if i % 3 == 1)
# for i in aset:
#     print(i)

# a = {1, 2, 3}
# b = {3, 4, 5}
# c = a & b
# print(c)



# def say1(*args):
#     print('My argument1 is', args)

# def say2(**args):
#     print('My argument2 is', args)

# say1(1, 3, 5)
# say2(a=1, b=2, c=3)


# def print_if_true(thing, check):
#     '''
#     Prints the first argument if the second argument is true.
#     '''
#     if check: 
#         print(thing)

# def print_songs(s, func):
#     for song in s:
#         print(func(song))

# songs = ['hello', 'hero', 'without you']
# print_songs(songs, lambda s: ''.join([s.capitalize(), '!']))

# def doc_it(func):
#     def doc_it_core(*args, **kwargs):
#         print(func.__name__, 'starting')
#         print('args', args)
#         print('kwargs', kwargs)
#         result = func(*args)
#         print(result)
#         print(func.__name__, 'completed')
#         return result
#     return doc_it_core

# @doc_it
# def add(a, b, **c):
#     return a + b

# add(5, 3, name='Howard')


