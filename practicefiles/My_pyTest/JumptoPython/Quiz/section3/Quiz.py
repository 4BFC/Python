# 03 section
# Q1
a = "Life is too short, you need python"

if "wife" in a:
    print("wife")  # x
elif "python" in a and "you" not in a:
    print("python")  # x
elif "shirt" not in a:
    print("shirt")  # o
elif "need" in a:
    print("need")  # o => true이지만 위의 조건문이 먼저
else:
    print("none")  # x

# Q2  ☆☆☆☆
result = 0
i  = 1
while i <= 1000:
    if i % 3 == 0 :
      result += i
      # print(result);
    i += 1
print(result)

# Q3 ☆☆☆
i = 0
while True:
    i += 1
    if i > 5 : break
    print('*' * i)

# Q4 ☆☆☆
for i in range(1, 101) : 
    print(i)

# Q5
A = [70, 60, 55, 75, 95, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total / len(A);
print(average)

# Q6 ☆☆☆☆☆☆
numbers = [1,2,3,4,5]
result = [n*2 for n in numbers if n % 2 == 1]
print(result)