# for문의 컴프리헨션과 if문을 사용한 짝수값 구하기
a = [1, 2, 3, 4]
result = [num*3 for num in a if num % 2 == 0]
print(result)
