#하나의 함수로 통합해보라 
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

num1 = int(input("첫 번째 정수 : "))
num2 = int(input("두 번째 정수 : "))
op = input("연산자 입력 : ")

if op == "+":
    res = add(num1, num2)
elif op == "-":
    res = subtract(num1, num2)
elif op == "*":
    res = multiply(num1, num2)
elif op == "/":
    res = divide(num1, num2)
else : print(op + "는 잘못된 연산자 입니다.")

print(num1, op, num2, '=', res)
