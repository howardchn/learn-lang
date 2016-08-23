class Person:

    def __init__(self, name):
        self.__name = name
        self.__age = 16

    def get_name(self):
        print('get_name called.')
        return self.__name

    def set_name(self, name):
        print('set_name called.')
        self.__name = name

    name = property(get_name, set_name)

    @property
    def age(self):
        print('get_age called.')
        return self.__age

    @age.setter
    def age(self, age):
        print('set_age called.')
        self.__age = age

howard = Person('Howard')

howard.name = 'Howard Chen'
howard.age = 34
print(howard.name)
print(howard.age)
print(howard._Person__name)