# https://www.acmicpc.net/problem/2470
n = int(input())
data = list(map(int,input().split()))
data.sort() # 오름차순 정렬


# 이분탐색 수행
start,end = 0,n-1

max_size = abs(data[start] + data[end])
sol1,sol2 = data[start],data[end]

while start<end:
    # 양 끝값을 더했을때의 특성값 
    solution = abs(data[start] + data[end])
    # 더 농도를 줄일 수 있다면 용액 업데이트
    if solution < max_size:
        max_size = solution
        sol1,sol2 = data[start],data[end]
        # 정답을 찾으면 종료
        if solution==0:
            break
    # 0과 가깝게 만드는 것이 목표이므로
    # 0과 비교하여 작은 값이라면 start를 앞으로 당기고, 크다면 end를 뒤로 당긴다.
    if data[start] + data[end]<0:
        start+=1
    else:
        end-=1
print(sol1,sol2)