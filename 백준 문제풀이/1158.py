# https://www.acmicpc.net/problem/1158

'''
요세푸스 문제는 다음과 같다.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 
양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 
한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 
이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 
예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.
'''
from collections import deque

# n명, k번째 사람 제거
n, k = map(int, input().split())

# n명의 사람을 원탁에 앉게 한다.
queue = deque(list(i for i in range(1, n+1)))

result = []  # 정답을 저장할 배열

# 원탁에 사람이 다 비워질때까지 알고리즘 수행
while queue:
    # k번째 사람 전까지 큐에서 사람을 뽑아 맨뒤로 순번을 넘긴다.
    for _ in range(k-1):
        # k번째 사람이 필요한것이므로, 그전의 사람들은 무시한다.
        queue.append(queue.popleft())
    result.append(queue.popleft())  # k번째 사람을 큐에서 제거하고, result배열에 삽입한다.

# 알고리즘 종료 후 정답 출력
print('<', end='')
for i in range(n):
    if i == n-1:  # 마지막번호는 >로 마무리
        print(result[i], end='>')
    else:
        print(result[i], end=', ')
