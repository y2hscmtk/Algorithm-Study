# 나이트의 이동경로를 steps 변수에 넣고 2가지 이동 규칙에 따라 다음과 같이 대입이 가능하다

# steps = [(-2,1),(-1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)] 

# 이제 나이트의 현재 위치가 주어지면 현재 위치에서 이동 경로를 더한 다음 8x8 좌표 평면에 있는지 확인하면 된다.
 
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1 #알파벳으로 입력된 정보를 숫자로 변환

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2,1),(-1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)] 

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인

result = 0
for step in steps:
    #이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >=1 and next_row <=8 and next_column >= 1 and next_column <= 8:
        result+=1 #이동가능하면 경우의 수 한가지 추가
        
print(result)