# 181 ~ 190
# 181
# 아래 표에서 하나의 행을 하나의 리스트로, 총 3개의 리스트를 갖는 이차원 리스트 apart를 정의하라.

# 101호	102호
# 201호	202호
# 301호	302호
# 정답확인


from audioop import reverse


apart = [[101,102],[201,202],[301,302]]
print(apart)

# 182
# 아래 표에서 하나의 열을 하나의 리스트로, 총 2개의 리스트를 갖는 이차원 리스트 stock을 정의하라.

# 시가	종가
# 100	80
# 200	210
# 300	330
# 정답확인

stock = [['시가', 100, 200, 300],['종가', 80, 210, 330]]
print(stock)

# 183
# 아래 표를 stock 이름의 딕셔너리로 표현하라.시가를 key로 저장하고, 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다. 종가 역시 key로 저장하고 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다.

# 시가	종가
# 100	80
# 200	210
# 300	330
# 정답확인

#value = {{'시가':'종가'},{100:80},{200:210},{300:330}}
value = {'시가':'종가',100:80,200:210,300:330}
print(value)
#solution
value = {'시가':[100,200,300],'종가':[80,210,330]}
print(value)

# 184
# 아래 표를 stock 이라는 이름의 딕셔너리로 표현하라. 날짜를 key로 저장하고, 나머지 같은 행의 데이터를 리스트로 저장해서 value로 저장한다. 첫 열이 날짜이다.

# 10/10	80	110	70	90
# 10/11	210	230	190	200
# 정답확인

stock = {'10/10':[80,110,70,90],'10/11':[210,230,190,200]}
print(stock)
# 185
# 리스트에 저장된 데이터를 아래와 같이 출력하라.

# apart = [ [101, 102], [201, 202], [301, 302] ]
# 101 호
# 102 호
# 201 호
# 202 호
# 301 호
# 302 호
# 정답확인

apart = [ [101, 102], [201, 202], [301, 302] ]
# print(apart[[0]])
# test = '1,2,3'
# print(test.split(','))

for i in apart:
  #print(i)
  for j in i:
     print(j,'호')


print("------------")
# 186
# 리스트에 저장된 데이터를 아래와 같이 출력하라.

# apart = [ [101, 102], [201, 202], [301, 302] ]
# 301 호
# 302 호
# 201 호
# 202 호
# 101 호
# 102 호
# 정답확인
apart = [ [101, 102], [201, 202], [301, 302] ]
apart.reverse()
for i in apart:
  #print(i)
  for j in i:
     print(j,'호')
     

#solution
print("------------")
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::-1]:
  #print(i)
  for j in i:
     print(j,'호')

# 187
# 리스트에 저장된 데이터를 아래와 같이 출력하라.

# apart = [ [101, 102], [201, 202], [301, 302] ]
# 302 호
# 301 호
# 202 호
# 201 호
# 102 호
# 101 호
# 정답확인
print("------------")
apart = [ [101, 102], [201, 202], [301, 302] ]
apart.reverse()

for i in apart:
  #print(i)
  i.reverse()
  for j in i:
     print(j,'호')

# 188
# 리스트에 저장된 데이터를 아래와 같이 출력하라.

# apart = [ [101, 102], [201, 202], [301, 302] ]
# 101 호
# -----
# 102 호
# -----
# 201 호
# -----
# 202 호
# -----
# 301 호
# -----
# 302 호
# -----
# 정답확인

apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
  for j in i:
    print(j)
    print('-----')


#solution
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
  for j in i:
    print(j,'호')
    print('-'*5)
  

# 189
# 리스트에 저장된 데이터를 아래와 같이 출력하라.

# apart = [ [101, 102], [201, 202], [301, 302] ]
# 101 호
# 102 호
# -----
# 201 호
# 202 호
# -----
# 301 호
# 302 호
# -----

apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
  for j in i:
    print(j)
  print('-----')

# 정답확인
# 190
# 리스트에 저장된 데이터를 아래와 같이 출력하라.

# apart = [ [101, 102], [201, 202], [301, 302] ]
# 101 호
# 102 호
# 201 호
# 202 호
# 301 호
# 302 호
# -----
# 정답확인

apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
  for j in i:
    print(j)
print('-----')