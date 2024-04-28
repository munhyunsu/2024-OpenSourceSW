num = input('정수 혹은 소수를 입력하세요: ')
print(f'num의 자료형: {type(num)}')

float_num = float(num)
print(f'입력한 숫자의 소수형: {float_num}')
print(f'float_num의 자료형: {type(float_num)}')

int_num = int(float(num))
print(f'입력한 숫자의 정수형: {int_num}')
print(f'int_num의 자료형: {type(int_num)}')

