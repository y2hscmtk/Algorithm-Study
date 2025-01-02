# HashMap / 세 수의 합
'''
n개의 정수가 입력으로 주어지고, 이 중 서로 다른 세 개의 위치를 골라 각 위치에 있는 세 수를 더했을 때 k가 되는 서로 다른 조합의 개수를 출력하는 코드를 작성해보세요.
'''
n, k = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
for i in range(n):
    count = dict()
    num1 = arr[i]
    # k - num1을 만들 수 있는 경우의 수
    for j in range(i+1,n):
        num2 = arr[j]
        target = k - num1 - num2
        if target in count:
            result += count[target]
        if num2 in count:
            count[num2] += 1
        else:
            count[num2] = 1

print(result)
