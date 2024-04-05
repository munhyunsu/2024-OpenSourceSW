class Dog:
    kind = '보더콜리'

    def __init__(self, name):
        self.name = name


a = Dog('하나')
a.name = 'One'
a.kind = 'Cat'
b = Dog('둘')
Dog.kind = '고양이'

print(f'a의 종: {a.kind}, 이름: {a.name}')
print(f'b의 종: {b.kind}, 이름: {b.name}')

