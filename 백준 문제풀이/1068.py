# https://www.acmicpc.net/problem/1068

'''
트리에서 리프 노드란, 자식의 개수가 0인 노드를 말한다.

트리가 주어졌을 때, 노드 하나를 지울 것이다. 

그 때, 남은 트리에서 리프 노드의 개수를 구하는 프로그램을 작성하시오. 

노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거된다.

예를 들어, 다음과 같은 트리가 있다고 하자.


현재 리프 노드의 개수는 3개이다. 

(초록색 색칠된 노드) 이때, 1번을 지우면, 다음과 같이 변한다. 

검정색으로 색칠된 노드가 트리에서 제거된 노드이다.

이제 리프 노드의 개수는 1개이다.
'''

# 정점의 개수
n = int(input())

# 부모에 대한 정보 입력받기
parent = list(map(int, input().split()))

remove = int(input())

# dfs를 통하여 제거 대상와 그 자식들 전부 제거


def DFS(remove):
    # True는 제거되었다는 의미
    parent[remove] = -2
    # remove의 자식들도 모두 제거
    for i in range(n):
        # 제거된 대상을 부모로 하는 노드가 있다면
        if parent[i] == remove:
            DFS(i)  # 해당 노드도 제거처리


# 제거 처리
DFS(remove)

# parent배열에서 중복값 제거 => 같은 부모

count = 0
for i in range(len(parent)):
    # 제거되지 않은 노드이면서, 해당 노드를 부모로 삼지 않아야함
    if parent[i] != -2 and i not in parent:
        count += 1

print(count)
