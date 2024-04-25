class Dog:
    kind = '보더 콜리'

    def __init__(self, name):
        self.name = name
        self.tricks = set()

    def add_trick(self, trick):
        self.tricks.add(trick)


a = Dog('하나')
b = Dog('둘')

a.add_trick('앉아!')
a.add_trick('손!')
b.add_trick('물어와!')

print(f'a의 종: {a.kind}, 이름: {a.name}, 기술: {a.tricks}')
print(f'b의 종: {b.kind}, 이름: {b.name}, 기술: {b.tricks}')

