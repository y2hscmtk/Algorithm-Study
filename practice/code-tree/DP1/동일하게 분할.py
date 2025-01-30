'''
n개의 수가 주어졌을 때, 정확히 2개의 그룹 A,B로 나누어
A에 들어있는 수의 합과 B에 들어있는 수의 합이 일치하도록 작성

-> 중복 불가

=> 모든 수를 일단 한 그룹에 몰아 넣는다고 생각, 절반 만큼을 만들 수 있는지 없는지 여부로 판단

동전 만들기 유형 생각

한번씩만 숫자를 사용하여 모든 n개의 수의 합의 절반만큼을 만들 수 있는지 여부를 판단
'''
n = int(input())
numbers = list(map(int,input().split()))

total_sum = sum(numbers)

if total_sum % 2 != 0: # 홀수인 경우는 절반으로 분리 못함
    print('No')
else:
    target = total_sum//2
    dp = [False]*(target+1) # 정확히 절반을 만들면 성공
    dp[0] = True # 0을 만들 수 있는 방법은 무조건 존재

    for num in numbers:
        # 중복없이 수를 선택하기 위해 거꾸로 DP 설정
        for i in range(target,-1,-1):
            # 현재 수(num)을 추가함으로서 i를 만들 수 있는 경우가 있는지 파악
            if i-num >= 0 and dp[i-num] == True: # i-num을 만들 수 있는 방법이 존재한다면
                dp[i] = True

    if dp[-1]:
        print("Yes")
    else:
        print("No")
