n, k = map(int, input().split())

# 파스칼의 삼각형 만들기
# 기본적으로 모두 1로 초기화하고
# 위의 수를 더해서 만든다는 규칙대로 생성
# 줄은 n번째 줄까지
pascal = [[1]*n for _ in range(n)]
for i in range(2, n):
    for j in range(1, i):
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

# 정답 출력
print(pascal[n-1][k-1])
