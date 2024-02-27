# https://www.acmicpc.net/problem/1687
'''
각 0에 대해서 자신을 포함하여 자신의 위에 있는 0의 개수에 대해 높이 배열을 만든다.
(= 히스토그램)
각 행에 대해서 면적 계산을 수행한다.
각 행에 대해서 현재 행까지의 높이는 이전에 초기화를 해뒀으므로 알 수 있고, 
'''
N, M = map(int,input().split())
s = [list(input()) for _ in range(N)]

# 각 칸에 대해 해당 칸을 포함하여 위로 연속된 0의 개수를 저장하는 행렬 생성
height = [[0]*M for _ in range(N)]

# 첫 번째 행에 대한 처리
for j in range(M):
    height[0][j] = 1 if s[0][j] == '0' else 0

# 두 번째 행부터 N번째 행까지 처리
for i in range(1, N):
    for j in range(M):
        if s[i][j] == '0':
            height[i][j] = height[i-1][j] + 1
        else:
            height[i][j] = 0
            
# 스택을 활용해서 현재 자신의 높이보다 더 높은 높이를 만나기 전까지 이어나갈 수 있음
# 예를 들어 높이가 아래와 같을때
# 0 1 3 2 3
#       | 이 위치에 있을 때 스택에 현재까지 삽입된 결과가 아래와 같다.
# [(0,0),(1,1),(2,3)]
# 높이는 현재 2인 상황에서 직전의 높이가 현재 자신보다 높으므로 스택에 쌓지 못한다.
# (높이가 같아야 같은 길이로 계속해서 계산이 가능하다.)
# i = 3, h = 2
# => 이전 계속해서 팝한다.(높이가 3인 지점이 언제까지 이어지는지 구하기 위함(index 업데이트) => i-index 가로 길이)
# (2,3) => index = 2 height = 3, height * (i-index) = 3*(3-2) = 3
# for h in height:
#     print(*h)
    
def largestRectangleArea(heights):
    stack = []
    max_area = 0
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            max_area = max(max_area, height * (i - index))
            start = index
        stack.append((start, h))
    for i, h in stack:
        max_area = max(max_area, h * (len(heights) - i))
    return max_area

# 각 행에 대해 히스토그램의 최대 직사각형 면적을 찾아 최댓값을 구함
answer = 0
for i in range(N):
    answer = max(answer, largestRectangleArea(height[i]))
print(answer)