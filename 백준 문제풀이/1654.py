# # https://www.acmicpc.net/problem/1654

k,n = map(int,input().split())
# 전체 전선의 개수 입력받기
lines = []

for _ in range(k):
    lines.append(int(input()))

low,high = 1,max(lines)


# 조건 설정
def check(m):
    temp = 0 # 만들 수 있는 전선의 개수
    for line in lines:
        temp += (line//m) # m으로 나누어서 얻는 몫만큼 전선을 얻을수있음
        
    # m으로 잘라서 얻은 전체 전선의 개수가 n개를 넘어선다면 True
    if temp>=n:
        return True
    else:
        return False
    

# 이분탐색 수행
while low<=high:
    mid = (low+high)//2
    # 조건을 만족할때
    if check(mid):
        # 조건을 만족시킨다면 더 높은 길이로도 조건을 만족하는지 확인해야함
        # 최대 렌선의 길이를 구하는것이 목표이므로
        low = mid+1
        result = mid
    else:
        # 아니라면 길이를 더 줄여야함
        high = mid-1
print(result)
            
