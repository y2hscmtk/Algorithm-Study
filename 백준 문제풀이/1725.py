
import sys
input = sys.stdin.readline
stack = []
result = 0 # 최대 넓이 
n = int(input())
for i in range(n):
    h = int(input())
    keep = i # 아직 사용하지 않은 높이 저장용
    while stack and stack[-1][1] > h: # 현재 높이보다 낮거나 같아질 때까지 반복(넓이 구하기)
        # 각각 수행
        # 스택에서 팝한 높이 * 인덱스 차(가로) = 넓이
        index,height = stack.pop() # 스택에서 팝한 높이, 인덱스
        result = max(result,(height*(i-index))) # 넓이 갱신
        keep = index # 저장 범위 갱신(낮아지는 순간 바로 다음에 적어도 마지막 높이 이상의 값이 있음)
        # 높이가 낮아지는 경우를 만날 경우 넓이 계산 종료, 아직 사용하지 않은 높이에 대해서 스택에 삽입
    stack.append((keep,h)) # 낮아지는 순간 바로 다음에 적어도 마지막 높이 이상의 값이 있음, 첫번째 값의 경우 바로 삽입
# 아직 스택에 남아 있는 수들은 모두 오름차순으로 정렬되어있는 형태
# i는 keep범위로 되어있다.
for i,h in stack:
    result = max(result,h*(n-i)) # 현재 인덱스부터 끝까지는 적어도 높이 h가 보장됨
print(result)