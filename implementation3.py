# 왕실의 나이트

# 8 x 8 의 좌표평면에서 나이트가 이동한다. 나이트는 다음과 같은 규칙대로 이동이 가능하다.

# 0. 나이트는 좌표평면 밖으로 이동할 수 없다.
# 1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
# 2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기

# 이처럼 8x8좌표평면에서 나이트의 위치가 주어졌을때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오

# 왕실의 정원에서 행 위치를 표현할 때는 1부터 8로 표현하고, 열 위치를 표현할 때는 a부터 h로 표현한다.

# 입력예시: a1(나이트의 위치) 출력 예시: 2(경우의 수)

point = input()

row = point[0] #열 정보(a,b,c//)
line = int(point[1]) #행 정보(1,2,3//)
result =0 

if 'c'<=row<='f' and 3<=line<=6:
    result = 8 #C3~f3~C3~C6 범위의 경우 이동할 수 있는 경우의 수 8가지 발생
elif (line==2 or line==7) and 'c'<=row<='f':
    result = 6 #파란색 영역
elif 3<=line<=6 and (row=='b'or row=='g'):
    result = 6 #파란색 영역
elif (line==2 or line==7) and (row=='b' or row=='g'):
    result = 4 #검은색 영역
elif (line==1 or line==8) and 'b'<=row<='g':
    result = 3 #빨간색 영역
elif 2<=line<=7 and (row=='a'or row=='h'):
    result = 3 #빨간색 영역
else:
    result = 2 #각 꼭짓점
    
print(result)    

#아이디어&코딩 24분 57초 소요