name = input("==> 이름을 입력하세요:")
order = input("==> 어떤 음료를 주문하시겠어요?")
number = int(input("==> 몇 잔 드릴까요?"))
print()
print("%s님은 %s를 %d잔 주문하셨습니다." %(name, order, number))
print(f"{name}님은 {order}를 {number}잔 주문하셨습니다.")
