# https://www.acmicpc.net/problem/10973
'''
-1을 출력하게 되는 상황 => 모든 수가 내림차순인 상황
모든 수가 내림차순이 아니라면? => '이전 수'를 만들 수 있다.
문제의 접근 방법은 현재 수의 '이전 수'를 바로 찾는 것 => 조합을 사용하면 시간초과에 걸린다. 10000_P_10000 이므로..

'''
import sys
n = int(input())
current = list(map(int, input().split()))  # 현재 수 입력받기

# 이미 가장 작은 수인지 확인
array = [i for i in range(1, n+1)]
if current == array:
    print(-1)
    sys.exit(0)

# 뒤에서부터 오름차순을 만족하는 구간 확인
for i in range(n-1, -1, -1):
    # 5,3,1,2,4 => 3 > 1 이므로, 3 이하의 수에서는 오름차순
    if current[i-1] > current[i]:
        target = i-1
        break


# 타겟 이후의 수들 중에서 타겟보다 작은 수 중에서 가장 큰 수 찾기
# 뒤의 배열은 이미 오름차순 이므로, 뒤에서부터 찾으면 조건을 만족하는 가장 큰 수를 찾을 수 있다.
for i in range(n-1, target, -1):
    if current[i] < current[target]:
        index = i  # 인덱스 저장
        break

# 타겟 수와 자리 바꾼 후, 이후의 수는 내림차순으로 정렬(이전 수)
current[target], current[index] = current[index], current[target]
result = current[:target+1] + sorted(current[target+1:n], reverse=True)
print(*result)
