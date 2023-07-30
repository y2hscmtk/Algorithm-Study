# https://www.acmicpc.net/problem/2792
'''
'질투심'은 가장 많이 가지고 있는 학생의 보석의 수
질투심을 최소가 되도록 하기 위해 => 최대 '몇개'를 나눠줄지 결정
해당 개수로 나눠줄때 같은 색상을 유지하면서 N명의 학생에게 나눠줄수 있는지 확인
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # 아이들의 수, 색상의 수
candy = [int(input().strip()) for _ in range(m)]  # 각 색상별 사탕의 수

max_candy = max(candy)
result = max_candy
# 사탕을 최소 몇개 나눠줄 지 결정 => mid = 나눠줄 사탕의 수
start, end = 1, max_candy
'''
7 5
7 1 7 4 4
start,end = 1,7 => mid = 4
# 4개씩? => 모두 나눠줄 수 있음
(4,3),(1),(4,3),4,4 => 7명에게 나눠줄 수 있음 굿!
'''
while start <= end:
    mid = (start+end)//2
    # 가장 많은 양의 사탕이 mid개보단 많이 있어야 함
    # => 그래야 나눠줄 수 있을테니까
    if max_candy < mid:
        end = mid - 1  # 사탕의 개수를 왼쪽 영역에서 결정
        continue

    # 모든 사탕을 최소 mid개 나눠줄 수 있다면 => 파라매트릭 서치 진행
    count = 0  # 몇명의 학생들에게 나눠줬는지
    for i in range(m):  # 색생의 개수만큼 반복
        temp = candy[i]  # 해당 색상의 사탕의 개수
        # 해당 색상의 사탕으로 나눠줄 수 있는 학생 수 계산
        if temp % mid == 0:  # 정확히 mid개씩 나눠줄 수 있는 경우
            count += (temp//mid)
        else:  # mid개씩 나눠주고 나머지가 남는 경우 => 나머지는 모두 한명에게 지급
            count += (temp//mid + 1)

    # 몇명의 학생들에게 나눠줬는지 확인
    if count > n:  # 너무 조금씩 나눠줬다 => 더 많이 나눠줄 수 있는지 확인
        start = mid + 1
    else:  # n명 이하의 학생들에게 나눠줬다
        # 더 조금씩 나눠줘도 조건을 만족하는지 확인
        end = mid - 1  # 왼쪽 영역에서 재탐색
        # 보석을 받지 못하는 학생이 있어도 된다!!!
        result = min(result, mid)  # 정답 최소값으로 갱신

print(result)
