# https://www.acmicpc.net/problem/15658

'''
첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 
둘째 줄에는 A1, A2, ..., AN이 주어진다. 
(1 ≤ Ai ≤ 100) 셋째 줄에는 합이 N-1보다 크거나 같고, 
4N보다 작거나 같은 4개의 정수가 주어지는데, 
차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다. 
'''
n = int(input())
# 숫자 배열
number = list(map(int, input().split()))
# 연산자 개수
# +,-,*,//
operator = list(map(int, input().split()))

max_num, min_num = -(10**8), 10**8


# 백트래킹
# 현재 연산에 이용하는 숫자(num), 현재 수가 몇번째 수인지(i)
def calc(num, i):
    global max_num, min_num
    if i+1 == n:  # 모든 수를 다 계산하였다면
        # 최대값 최소값 업데이트
        max_num = max(num, max_num)
        min_num = min(num, min_num)
        return  # 반복 종료
    for j in range(4):
        if operator[j] != 0:  # 연산자가 남아있다면
            operator[j] -= 1
            if j == 0:  # 더하기 연산의 경우
                calc(num+number[i+1], i+1)  # 해당 연산의 수행 결과를 넘김
            elif j == 1:  # 빼기 연산의 경우
                calc(num-number[i+1], i+1)  # 해당 연산의 수행 결과를 넘김
            elif j == 2:  # 곱하기 연산의 경우
                calc(num*number[i+1], i+1)  # 해당 연산의 수행 결과를 넘김

            # 음수를 양수로 나눌 때는 C++14의 기준을 따른다.
            # 즉, 양수로 바꾼 뒤 몫을 취하고 그 몫을 음수로 바꾼 것과 같다
            elif j == 3:  # 나누기 연산의 경우
                calc(abs(abs(num)//number[i+1]), i+1)  # 해당 연산의 수행 결과를 넘김
            operator[j] += 1


calc(number[0], 0)
print(max_num)
print(min_num)
