x = int(input('짝수를 출력합니다. 어디까지 출력할까요? '))

for number in range(x):
    if number % 2 == 0:
        print(number)

