# alphabet = 'abcdefg' +\
#     'hijklmn' +\
#     'opqrst' +\
#     'uvwxyz'

# print (alphabet)

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['Banana', 'Orange', 'Peach']
desserts = ['Coffee', 'Tea', 'Beer']

for day, fruit, dessert in zip(days, fruits, desserts):
    print ('day: %(day)s, fruit: %(fruit)s, dessert:%(dessert)s' %{'day':day, 'fruit':fruit, 'dessert':dessert})