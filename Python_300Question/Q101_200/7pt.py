# 161 ~ 170
# 161
# for문과 range 구문을 사용해서 0~99까지 한 라인에 하나씩 순차적으로 출력하는 프로그램을 작성하라.

# 정답확인

from audioop import reverse
from re import I


for l_ist in range(100):
  print(l_ist)

# 162
# 월드컵은 4년에 한 번 개최된다. range()를 사용하여 2002~2050년까지 중 월드컵이 개최되는 연도를 출력하라.

# 2002
# 2006
# 2010
# ...
# 2042
# 2046
# 2050
# 참고) range의 세번 째 파라미터는 증감폭을 결정합니다.

# >> print(list(range(0, 10, 2)))
# [0, 2, 4, 6, 8]
# 정답확인

print(list(range(2002,2051,4)))

for cup in range(2002,2051,4) :
  print(cup)

# 163
# 1부터 30까지의 숫자 중 3의 배수를 출력하라.

# 3 
# 6 
# 9 
# 12 
# 15 
# 18 
# 21 
# 24 
# 27 
# 30
# 정답확인

for thrird_x in range(3,31,3):
  print(thrird_x)


# 164
# 99부터 0까지 1씩 감소하는 숫자들을, 한 라인에 하나씩 출력하라.

# 정답확인

for mine_us in range(100) :
  print(99 - mine_us)
  

# 165
# for문을 사용해서 아래와 같이 출력하라.

# 0.0
# 0.1
# 0.2
# 0.3
# 0.4
# 0.5
# ...
# 0.9
# 정답확인
i = 0
for i in range(10) :
  print(float(i/10))

# 166
# 구구단 3단을 출력하라.

# 3x1 = 3
# 3x2 = 6
# 3x3 = 9
# 3x4 = 12
# 3x5 = 15
# 3x6 = 18
# 3x7 = 21
# 3x8 = 24
# 3x9 = 27
# 정답확인

for n in range(1,10):
  print('3x{}={}'.format(n,3*n))

# 167
# 구구단 3단을 출력하라. 단 홀수 번째만 출력한다.
# 3x1 = 3
# 3x3 = 9
# 3x5 = 15
# 3x7 = 21
# 3x9 = 27
# 정답확인

for oddn in range(1,10,2):
  print('3x{}={}'.format(oddn,3*oddn))

# 168
# 1~10까지의 숫자에 대해 모두 더한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.

# 합 : 55
# 정답확인
print('-------------')
tmp = 0
for i in range(0,11):
  tmp += i
  print(tmp)

# 169
# 1~10까지의 숫자 중 모든 홀수의 합을 출력하는 프로그램을 for 문을 사용하여 작성하라.

# 합: 25
# 정답확인
tmp = 0
for i in range(1,11,2):
  tmp += i
  print(tmp)

# 170
# 1~10까지의 숫자를 모두 곱한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.

tmp = 1
for i in range(1,11):
  tmp *= i
  print(tmp)

# 정답확인