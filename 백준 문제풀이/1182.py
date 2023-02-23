# https://www.acmicpc.net/problem/1182

'''
문제
N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. 
(1 ≤ N ≤ 20, |S| ≤ 1,000,000) 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 
주어지는 정수의 절댓값은 100,000을 넘지 않는다.

출력
첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.
'''
'''
1부터 배열의 길이까지 뽑을 숫자를 하나씩 늘려가며, 수를 더했을때 S가 되는지 확인하고
S라면 카운트를 증가시킨다.
(조합을 이용하면 해결할수 있을것같다.)
'''
from itertools import combinations
n, s = map(int, input().split())

# 숫자배열 입력받기
numbers = list(map(int, input().split()))

result = 0  # 경우의 수(정답)
# 배열에서 뽑을 숫자의 개수를 결정 1개부터 n개까지
for i in range(1, n+1):
    # 숫자배열에서 i개를 고르는 모든 조합계산,
    # 조합의 합이 s가 된다면 경우의 수 카운트를 증가시킨다.
    for data in combinations(numbers, i):
        if sum(data) == s:
            result += 1


print(result)
