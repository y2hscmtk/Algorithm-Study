# https://www.acmicpc.net/problem/1755
'''
문제
79를 영어로 읽되 숫자 단위로 하나씩 읽는다면 "seven nine"이 된다. 

80은 마찬가지로 "eight zero"라고 읽는다. 79는 80보다 작지만, 영어로 숫자 하나씩 읽는다면 "eight zero"가 "seven nine"보다 사전순으로 먼저 온다.

문제는 정수 M, N(1 ≤ M ≤ N ≤ 99)이 주어지면 M 이상 N 이하의 정수를 숫자 하나씩 읽었을 때를 기준으로 사전순으로 정렬하여 출력하는 것이다.

첫째 줄에 M과 N이 주어진다.

M 이상 N 이하의 정수를 문제 조건에 맞게 정렬하여 한 줄에 10개씩 출력한다.
'''
# 인덱스를 기준으로,eng_num[0] = zero, eng_num[1] = one.. 이런식으로 바꿀수 있도록
eng_num = ["zero", "one", "two", "three", "four",
           "five", "six", "seven", "eight", "nine", "ten"]

m, n = map(int, input().split())

stack = []  # 스택 생성 => 영어로 번역하여 삽입하고, 사전순으로 재정렬하기 위해
# 정답은 숫자로 출력해야하므로, 숫자도 같이 삽입한다.

for i in range(m, n+1):
    # 문자열로 생각하여 한 글자씩 영어로 번역
    english = ""
    for num in str(i):
        english += eng_num[int(num)]
    stack.append([english, i])

# 오름차순 정렬
stack.sort()

i = 0
# 한줄에 10개씩 출력한다.
for number in stack:
    if i != 10:
        print(number[1], end=' ')
        i += 1
    else:
        print("")
        print(number[1], end=' ')
        i = 1
