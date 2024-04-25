import time

print('로켓 발사 카운트 다운!')
for number in range(10, 0, -1):
    print(f'발사 {number}초 전!')
    time.sleep(1)
print(f'로켓 발사!')

