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

# 아이디어 : 3이 들어가는 경우의 수를 직접 여러번 조사 할 필요없이, 문제에서 주어지는 조건은 시간정보 N에 대한 것 이므로, 한 시간 당 3이 들어가는 모든 경우의 수를 계산하여 더하기
n = int(input())

# 00시 00분 00초에서 00시 59분 59초까지 3이 들어가는 모든 경우의 수
# 초 : 3, 13, 23, 30,31,32,33,34,35,36,37,38,39, 43, 53 => 15번
# 분 : 3, 13, 23, 30,31,32,33,34,35,36,37,38,39, 43, 53 => 15번

count = (n+1)*60*15 + (n+1)*60*15

print(count)