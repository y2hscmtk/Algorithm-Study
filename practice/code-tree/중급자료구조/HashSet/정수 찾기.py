# 정수 찾기
'''
수열 a와 수열 b가 주어졌을 때, 수열 b의 각 원소가 수열 a에 포함되는지 알아보는 프로그램을 작성하세요.
'''
n = int(input())
a = list(map(int,input().split()))
set_a = set(a) # 포함되는지 안되는지 여부만 확인하면 되므로, O(1)에 삽입과 삭제가 가능한 set 자료형 사용
m = int(input())
b = list(map(int,input().split()))
for target in b:
    if target in set_a:
        print(1)
    else:
        print(0)