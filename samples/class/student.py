class Student:
    def __init__(self, korean, english, math):
        self.korean = korean
        self.english = english
        self.math = math

    def average(self):
        return (self.korean + self.english + self.math) / 3


n = int(input('학생 수 입력 (N): '))
for i in range(1, n+1, 1):
    korean = int(input(f'{i}번째 학생의 국어 성적 입력: '))
    english = int(input(f'{i}번째 학생의 영어 성적 입력: '))
    math = int(input(f'{i}번째 학생의 수학 성적 입력: '))
    s = Student(korean, english, math)
    print(f'{i}번째 학생의 평균 점수: {s.average()}')


