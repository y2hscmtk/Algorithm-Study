# https://www.acmicpc.net/problem/2003

'''
문제
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 

이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)이 주어진다. 

다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.
'''
'''
아이디어 : 배열의 앞에서부터 반복하여 순서대로 수를 더하고, M이 되었다면 반복을 멈추고 다음수부터 이어서 그 과정을 반복한다.
이 과정에서 모든 경우의 수를 구한다.
'''
n, m = map(int, input().split())

number = list(map(int, input().split()))

result = 0  # 경우의 수의 개수를 기록할 변수

for i in range(n):
    number_sum = 0  # 숫자의 합을 누적시키기 위해
    for j in range(i, n):
        number_sum += number[j]  # 수를 누적시켜 더한후,
        if number_sum == m:  # 만들고자 하는 수가 되었는지 확인
            result += 1  # 만들고자 하는 수가 완성되었다면 경우의 수를 추가하고
            break  # 해당 수에 대한 반복을 종료한다.

print(result)
