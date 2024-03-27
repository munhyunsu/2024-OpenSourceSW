x = int(input('입력: '))
print(f'{x}를 2로 나누어봅니다.')
while True:
    x = x // 2
    print(f'x = {x}')
    if x < 10:
        print('x가 10보다 작아졌으므로 종료합니다.')
        break
    
