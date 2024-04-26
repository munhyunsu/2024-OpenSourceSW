import random

x = random.randint(1, 10)
result = x * random.randint(1, 100)
print(f'{x} x ? = {result}')
y = int(input('?에 들어갈 정답은? '))
if x * y == result:
    print('정답입니다.')
else:
    print('오답입니다.')

