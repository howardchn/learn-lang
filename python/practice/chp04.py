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
for i in aset:
    print(i)

