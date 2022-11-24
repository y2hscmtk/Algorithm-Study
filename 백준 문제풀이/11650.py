# https://www.acmicpc.net/problem/11650

# 백준 11650번 좌표 정렬하기
# x좌표가 증가하는 순으로,
# x좌표가 같아면, y좌표가 증가하는 순으로 정렬시켜 출력

'''
입력
5        
3 4
1 1
1 -1
2 2
3 3
출력
1 -1
1 1
2 2
3 3
3 4
'''

# 데이터 입력받기
n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

# 정렬하기 => 람다 조건식을 별도로 주지 않는다면
# 디폴트 상태로, 문제에서 바라는 상황대로 정렬이 이루어진다.
data.sort()

# 출력하기
for d in data:
    print(d[0], d[1])  # 차례로 데이터 출력하기
