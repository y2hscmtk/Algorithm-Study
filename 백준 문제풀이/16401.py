# https://www.acmicpc.net/problem/16401
'''
구하고자 하는 값 : 막대 과자의 최대 길이
'''
import sys
input = sys.stdin.readline
M, N = map(int, input().split())
cookies = list(map(int, input().split()))
start, end = 1, sys.maxsize  # 가능한 과자의 최소,최대 길이
result = 0  # 나눠줄 수 있는 막대과자의 최대 길이

while start <= end:
    mid = (start+end)//2  # 중간값을 막대과자의 길이로 설정
    # 모두 같은 길이의 과자를 나눠줘야함 => 한 막대과자를 쪼갤수 있음
    # 몇명에게 나눠줄 수 있는지 확인
    count = 0  # 몇명에게 나눠줬는지
    for cookie in cookies:
        count += (cookie//mid)  # mid개로 나눈 몫만큼 나눠줄 수 있음(사람 수)
        # 사람 수가 목표했던 수 보다 많아졌다 => 너무 작게 쪼갰다 => 범위를 오른쪽으로
        if count > M:
            break

    # 사람 수가 목표했던 수 보다 많다
    if count >= M:  # 너무 작게 쪼갰다.
        result = max(result, mid)  # 우리는 최대한 크게 쪼개고 싶음
        start = mid+1
    else:  # 사람 수가 목표했던 수보다 적거나 같다. => 너무 크게 쪼갰다.
        end = mid-1

print(result)
