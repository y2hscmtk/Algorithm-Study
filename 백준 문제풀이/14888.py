# https://www.acmicpc.net/problem/14888

'''
N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다.
또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다. 연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다.

우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다. 이때, 주어진 수의 순서를 바꾸면 안 된다.

예를 들어, 6개의 수로 이루어진 수열이 1, 2, 3, 4, 5, 6이고,

주어진 연산자가 덧셈(+) 2개, 뺄셈(-) 1개, 곱셈(×) 1개, 나눗셈(÷) 1개인 경우에는 총 60가지의 식을 만들 수 있다.
예를 들어, 아래와 같은 식을 만들 수 있다.

1+2+3-4×5÷6
1÷2+3+4-5×6
1+2÷3×4-5+6
1÷2×3-4+5+6
식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다.

또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 즉, 양수로 바꾼 뒤 몫을 취하고,
그 몫을 음수로 바꾼 것과 같다. 이에 따라서, 위의 식 4개의 결과를 계산해보면 아래와 같다.

1+2+3-4×5÷6 = 1
1÷2+3+4-5×6 = 12
1+2÷3×4-5+6 = 5
1÷2×3-4+5+6 = 7
N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.

첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100) 셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데,
차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다.
'''
from itertools import permutations
n = int(input())  # 수의 개수
number = list(map(int, input().split()))
operator_list = list(map(int, input().split()))
op = ["+", "-", "*", "/"]

# 최댓값과 최솟값을 저장할 변수
result_min = 10**8
result_max = -(10**8)

# 연산자 재정립
operator = []
for i in range(4):
    # 해당 연산자의 개수만큼 기록
    for j in range(operator_list[i]):
        operator.append(op[i])

# 모든 경우의 수에 대하여 브루트포스
# 모든 경우의 수를 구해야 하므로, 중복 허용
# n개의 수 사이에 들어 갈 n-1개의 연산자 선택
for select in permutations(operator, n-1):
    number_sum = number[0]  # 첫번째 숫자를 미리 넣어두고 연산자에 따라 연산수행
    for i in range(n-1):
        if select[i] == "+":
            number_sum += number[i+1]
        elif select[i] == "-":
            number_sum -= number[i+1]
        elif select[i] == "*":
            number_sum *= number[i+1]
        elif select[i] == "/":
            number_sum = int(number_sum / number[i+1])

    result_max = max(result_max, number_sum)
    result_min = min(result_min, number_sum)


# 만들수 있는 최대값과 최소값을 출력
print(result_max)
print(result_min)
