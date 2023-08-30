# https://www.acmicpc.net/problem/2473
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
data.sort() # 이분탐색을 위해 정렬
'''
왼쪽에서부터 숫자 하나씩 포커싱 잡고 투포인터 활용 양 끝수와 더해서 0에 가까운지 확인
0보다 작은 수라면, s를 오른쪽으로 늘려야함
0보다 큰 수라면, e를 줄여야함
'''
r1,r2,r3 = data[0],data[1],data[n-1]
result = sys.maxsize # 0에 근접한 수를 찾기 위함
for i in range(n-2):
    target = data[i]
    # 기준수와 더할 두 수 결정
    s,e = i+1,n-1
    while s<e:
        temp = data[s]+data[e]
        # 세 수를 더한 수가 0에 가까운지 확인
        if target + temp <= 0:
            # 이전에 찾은 수보다 더 0에 근접한 수라면 업데이트
            if abs(target + temp) <= abs(result):
                result = target + temp
                r1,r2,r3 = target,data[s],data[e]
            # 0보다 작은 수라면 s를 늘려야 함
            s+=1
        else: # 0보다 큰 수라면
            # 이전에 찾은 수보다 더 0에 근접한 수라면 업데이트
            if abs(target + temp) <= abs(result):
                result = target + temp
                r1,r2,r3 = target,data[s],data[e]
            e-=1
        

print(r1,r2,r3)