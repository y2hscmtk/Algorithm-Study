# 시각

# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지 모든 시각 중에서 3이 하나라도 포함되는
# 모든 경우의 수를 구하는 프로그램을 작성하시오. 예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로
# 세어야 하는 시각이다.
# 00시 00분 03초
# 00시 13분 30초

# 반면에 다음은 3이 하나도 포함되어 있지 않으므로 세면 안 되는 시각이다.

# 00시 02분 55초
# 01시 27분 45초

# 입력 조건 : 첫째 줄에 정수 N이 입력된다.
# 출력 조건 : 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력한다.

from http.client import CannotSendRequest


n = int(input())
count = 0
time = list(0,0,0) #시, 분, 초
check3 = list(3,13,23,33,43,53)

for i in range(n): #0시부터 작동 시작
    for s in range(60):
        time[2]+=1 # 1초씩 증가시킴
        for c in check3:
            if time[2]==c:
                count+=1 #3이 하나라도 들어가는 경우에 대해, 조건 하나 증가시키기
                

print(count)
