# https://www.acmicpc.net/problem/11999
'''
X와 Y를 적절히 더해서 M을 넘지않는 최대값 만들기
'''
result = -1
x,y,m = map(int,input().split())

for i in range(m//x+2):
    temp = x * i # x를 i개 더한 값
    for j in range(m//y+2):
        temp2 = temp + y*j # temp + y를 j개 더한 값
        # m을 넘어가지 않는 최대값이 되었는지 확인
        if temp2<=m and result<temp2:
            result = temp2 # 값 업데이트

print(result)
