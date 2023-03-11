# https://www.acmicpc.net/problem/11866

'''
문제
요세푸스 문제는 다음과 같다.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 

이제 순서대로 K번째 사람을 제거한다. 

한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 

이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 

예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 1,000)

출력
예제와 같이 요세푸스 순열을 출력한다.
'''
from collections import deque

n, k = map(int, input().split())

# 큐 생성(덱)
queue = deque()

# 요새푸스에 사용할 숫자 데이터 큐에 삽입
for i in range(1, n+1):
    queue.append(i)

print("<", end='')
# 큐에 데이터가 존재하는동안 반복
while len(queue) != 1:
    # k번째 데이터가 필요하므로 k-1번째 데이터까지는 뒤로 넘기기(무시)
    for i in range(k-1):
        # 숫자를 뽑았다가 꼬리에 다시 삽입
        queue.append(queue.popleft())
    # k번째 데이터 출력
    print(queue.popleft(), end=', ')

# 마지막으로 남아있는 숫자를 출력하고 프로그램 종료
print(queue.popleft(), end=">")
