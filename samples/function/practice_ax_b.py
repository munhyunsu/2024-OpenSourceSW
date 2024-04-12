def ax_b(a, b, x):
    return a*a*x + b


a = int(input('a: '))
b = int(input('b: '))
m = int(input('Max: '))

for x in range(0, m+1, 1):
    print(f'{a}x{a}x{x} + {b} = {ax_b(a, b, x)}')

