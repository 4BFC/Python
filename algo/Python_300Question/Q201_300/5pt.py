# 241 ~ 250
# 241 현재시간
# datetime 모듈을 사용해서 현재 시간을 화면에 출력해보세요.
# 정답확인

import datetime
import imp
from time import strftime
now = datetime.datetime.now()
print(now)

# 242 현재시간의 타입
# datetime 모듈의 now 함수의 리턴 값의 타입을 화면에 출력해보세요.
# 정답확인

print(now, type(now))

# 243 timedelta
# datetime 모듈의 timedelta를 사용해서 오늘로부터 5일, 4일, 3일, 2일, 1일 전의 날짜를 화면에 출력해보세요.

# 정답확인

# day = datetime.timedelta.days#오답
# print(day)

# 244 strftime
# 현재시간을 얻어온 후 다음과 같은 포맷으로 시간을 출력해보세요. strftime 메서드를 사용하세요.

# 18:35:01 
# 정답확인

print(strftime(str(now)))#오답

# 245 strptime
# datetime.datetime.strptime 메서드를 사용하면 문자열 형식의 시간을 datetime.datetime 타입의 시간 값으로 만들어줍니다. "2020-05-04"의 문자열을 시간 타입으로 변환해보세요.

# 정답확인

#print(datetime.datetime.strptime("2020-05-04")) # 오답

# 246 sleep 함수
# time 모듈, datetime 모듈을 사용해서 1초에 한 번 현재 시간을 출력하는 코드를 작성하세요.

# 정답확인


# 247 모듈 임포트
# 모듈을 임포트하는 4가지 방식에 대해 설명해보세요.

# 정답확인

"1. import문을 사용해서 해당 모듈을 임포트 한다."
'2. from을 사용한다.'
'3. as를 사용한다.'

# 248 os 모듈
# os 모듈의 getcwd 함수를 호출하여 현재 디렉터리의 경로를 화면에 출력해보세요.

# 정답확인

import os

call = os.getcwd()
print(call,type(call))


# 249 rename 함수
# 바탕화면에 텍스트 파일을 하나 생성한 후 os 모듈의 rename 함수를 호출하여 해당 파일의 이름을 변경해보세요.

# 정답확인

os.rename("C:/Users/Administrator/Desktop/Drive.txt","C:/Users/Administrator/Desktop/운전면허.txt")

# 250 numpy
# numpy 모듈의 arange 함수를 사용해서 0.0 부터 5.0까지 0.1씩 증가하는 값을 화면에 출력해보세요.

# 정답확인
