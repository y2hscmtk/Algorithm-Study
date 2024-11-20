'''
# 1. 조건 찾아서 반복문 분할하여 해결
# 2. 조건 찾아서 변수의 값을 바꿔가며 반복문에 적용
'''
for tc in range(1,int(input())+1):
    N = int(input())
    result = 0
    board = [list(map(int,input().strip())) for _ in range(N)]
    
    # 합을 더하기 위한 각 행의 s,e영역의 값 변경시키기
    M = N//2
    s = e = M
    for i in range(N):
        for j in range(s,e+1):
            result += board[i][j]
        if i < M:
            s-=1; e+=1
        else:
            s+=1; e-=1
    
    print(f'#{tc} {result}')