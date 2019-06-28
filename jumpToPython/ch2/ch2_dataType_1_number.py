# -*- coding:utf-8 -*-

# 정수형
print('정수형 - 그냥 숫자')
a = 123
print(a)
a = -178
print(a)
a = 0
print(a)
print ''
print ''

# 실수형
print('실수형 - 소수점 들어간 것')
a = 1.2
print(a)
a = -3.45
print(a)
a = 4.24e10
print(a)
a = 4.24e-10
print(a)
print ''
print ''

# 8진수와 16진수
print('8진수(0o)와 16(0x)진수')
a = 0o177
print(a)
a = 0xABC
print(a)
print ''
print ''

# 연산
print('연산')
a = 3
b = 4
print(a + b)
print(a * b)
print(a / (b * 1.0))  # 실수형으로 바꾸고 계산
print(a ** b)  # 제곱
print(a % b)  # 나머지
print(a // (b * 1.0))  # 실수형으로 바꾸고 계산하는데 나누고나서 나머지 버림
a = -7
b = 4
print(a / (b * 1.0))  # 음수 나누기할때 주의
print(a // (b * 1.0))  # 음수 나누기할때 주의 - 가우스 생각
a = -5
b = 4
print(a / (b * 1.0))  # 반올림이 아니라 버림이라는 것 확인
print(a // (b * 1.0))  # 반올림이 아니라 버림이라는 것 확인
print ''
print ''

# 연습문제
print('=' * 30)
print('연습문제!!!!!')
print('=' * 30)
print('문제 1 : A, B, C 세 학생의 점수 평균 값 구하기')
print('A = 80, B = 75, C = 55')
a = 80
b = 75
c = 55
avg = (a + b + c) / 3.0
print(avg)
print('A, B, C 학생의 평균은 %s 입니다.' % avg)
print ''
print('문제 2 : 17을 3으로 나누었을 때 그 몫을 구하시오.')
a = 17
b = 3
res = 17 // 3
print(res)
print('17을 3으로 나누었을 때 몫은 %d 입니다.' % res)
print ''
print('문제 3 : 17을 3으로 나누었을 때 그 나머지 값을 구하시오.')
a = 17
b = 3
res = a % b
print('17을 3으로 나누었을 때 나머지는 %d 입니다.' % res)
print ''
print('문제 4 : 주어진 자연수가 홀수인지 짝수 인지 판별할 수 있는 방법에 대해서 말해보자')
print('2로 나누어 나머지가 1이면 홀수 0이면 짝수')
print ''
print('문제 5 : 17 / 3를 소수점 4자리까지만 구해라')
print(17 / (3 * 1.0))
print(round(17 / (3 * 1.0), 4))
