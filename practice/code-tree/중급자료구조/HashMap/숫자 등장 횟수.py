# HashMap / 숫자 등장 횟수
'''
n개의 숫자로 이루어진 수열 정보가 하나 주어졌을 때, m번에 걸쳐 특정 숫자가 주어지면 해당 숫자가 수열에 몇 개 있는지를 출력하는 프로그램을 작성해보세요.

첫 번째 줄에는 원소의 개수 n과 질의의 수 m이 공백을 사이에 두고 주어집니다.

두 번째 줄에는 n개의 원소가 공백을 사이에 두고 주어집니다.

세 번째 줄에는 m개의 숫자가 공백을 사이에 두고 주어집니다.

1 ≤ m ≤ n ≤ 100,000

1 ≤ 주어지는 원소, 숫자 값 ≤ 10^9

배열의 범위를 고려하여, 딕셔너리를 활용하여 사용 빈도수를 저장한다면 n만큼의 메모리를 사용하면서 O(1)에 접근 가능
'''
n,m = map(int,input().split())
d = {}

numbers = list(map(int,input().split()))

# 각 숫자가 몇번 등장하였는지 체크
for num in numbers:
    if num in d:
        d[num] += 1
    else:
        d[num] = 1

data = list(map(int,input().split()))

# 등장 횟수 반환
for num in data:
    if num in d:
        print(d[num], end=' ')
    else:
        print(0,end=' ')
    