# 길이가 N인 수열이 주어졌을 때, 그 수열의 합을 구하려고 한다. 하지만, 그냥 그 수열의 합을 모두 더해서 구하는 것이 아니라,

# 수열의 두 수를 묶으려고 한다. 어떤 수를 묶으려고 할 때, 위치에 상관없이 묶을 수 있다.

# 하지만, 같은 위치에 있는 수(자기 자신)를 묶는 것은 불가능하다. 그리고 어떤 수를 묶게 되면, 수열의 합을 구할 때 묶은 수는 서로 곱한 후에 더한다.

# 예를 들면, 어떤 수열이 {0, 1, 2, 4, 3, 5}일 때, 그냥 이 수열의 합을 구하면 0+1+2+4+3+5 = 15이다.

# 하지만, 2와 3을 묶고, 4와 5를 묶게 되면, 0+1+(2*3)+(4*5) = 27이 되어 최대가 된다.

# 수열의 모든 수는 단 한번만 묶거나, 아니면 묶지 않아야한다.

# # 수열이 주어졌을 때, 수열의 각 수를 적절히 묶었을 때, 그 합이 최대가 되게 하는 프로그램을 작성하시오.

'''
백준 1744번 재도전

생각가능한 시나리오는 다음과 같다.
1. 양수인 경우
2. 음수인 경우
3. 0인 경우

양수인 경우에 대해서, 
1인 경우는 다른 수와 곱하지 않고 더한다.
양수는 큰수끼리 곱하면 더 커진다.

음수인 경우에 대해서, 음수는 음수끼리 곱하면 양수가 되고, 이 경우에는 작은 음수끼리 곱하고 남은 수를 더하는것이 이득이다.
(-1,-2,-3) => 6-1 = 5 (max)

0인 경우에 대해서,
음수가 1개 있을경우, 해당 음수와 곱해서 음수를 제거하는것이 이득이다.
음수가 2n개 있을경우, 음수끼리 곱하면 양수가 되므로 배열에서 0을 제거하는것이 이득이다.
음수가 2n+1개 있을경우, 음수들 중, 가장 큰값(-1)과 곱해서 제거하는것이 이득이다.(나머지 2개의 음수끼리 곱하면 되기때문이다.)
음수가 없는 경우는 배열에서 제거하는것이 이득이다.

다음 상황에 맞게 그리디 알고리즘을 적용시키면 문제 해결이 가능할것으로 보인다.
'''

n = int(input())
zero = []  # 0을 저장할 배열
one = []
possitive_array = []  # 양수를 저장할 배열
negative_array = []  # 음수를 저장할 배열
max_sum = 0

for _ in range(n):
    number = int(input())
    if number > 1:
        possitive_array.append(number)
    elif number < 0:
        negative_array.append(number)
    elif number == 0:
        zero.append(number)
    else:
        one.append(number)

possitive_array.sort(reverse=True)  # 오름차순
negative_array.sort(reverse=True)  # 내림차순 -1, -2, -3 ...

# 최대합 구하는 과정

# 0단계: 1은 어떤수와도 연관되지 않고 그냥 더한다.
max_sum = sum(one)

# 1단계: 양수 배열에서 2개씩 곱해가며 더한다.
for i in range(0, len(possitive_array), 2):
    if i+1 < len(possitive_array):
        # 가장 큰수와 두번째로 큰수를 곱해서 더한다.
        max_sum += (possitive_array[i]*possitive_array[i+1])
    else:
        # 양수가 홀수개 있을경우 홀로 남은 수는 더한다.
        max_sum += possitive_array[i]

# 2단계: 0처리
if len(zero) != 0:
    # 0은 음수와 곱하는 과정을 통해 음수를 제거할수 있다.
    # 음수가 짝수개 일 경우 음수끼리 곱해서 양수를 만드는것이 이득이므로
    # 0은 모두 무시한다.
    if len(negative_array) % 2 != 0:  # 음수가 홀수개인 경우만 해당 계산 진행
        # 가장 큰 음수를 제거하면 나머지 값들을 곱하여 최대값으로 만들 수 있다!
        del negative_array[0]

negative_array.sort()  # 오름차순 정렬 -3,-2,-1...
# 3단계: 음수 처리
for i in range(0, len(negative_array), 2):
    if i+1 < len(negative_array):
        max_sum += (negative_array[i]*negative_array[i+1])
    else:
        max_sum += negative_array[i]

print(max_sum)
