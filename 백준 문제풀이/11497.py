'''
백준 11497번
https://www.acmicpc.net/problem/11497

남규는 통나무를 세워 놓고 건너뛰기를 좋아한다. 
그래서 N개의 통나무를 원형으로 세워 놓고 뛰어놀려고 한다. 남규는 원형으로 인접한 옆 통나무로 건너뛰는데, 
이때 각 인접한 통나무의 높이 차가 최소가 되게 하려 한다.

통나무 건너뛰기의 난이도는 인접한 두 통나무 간의 높이의 차의 최댓값으로 결정된다. 
높이가 {2, 4, 5, 7, 9}인 통나무들을 세우려 한다고 가정하자. 
이를 [2, 9, 7, 4, 5]의 순서로 세웠다면, 가장 첫 통나무와 가장 마지막 통나무 역시 인접해 있다.
즉, 높이가 2인 것과 높이가 5인 것도 서로 인접해 있다. 배열 [2, 9, 7, 4, 5]의 난이도는 |2-9| = 7이다. 
우리는 더 나은 배열 [2, 5, 9, 7, 4]를 만들 수 있으며 이 배열의 난이도는 |5-9| = 4이다.
이 배열보다 난이도가 낮은 배열은 만들 수 없으므로 이 배열이 남규가 찾는 답이 된다.

'''

'''
아이디어 : 통나무 배열을 오름차순으로 정렬한뒤
작은 순서대로 양끝에 놓으면 되지않을까?
예:
10 10 11 11 12 12 13
10 11 12 13 12 11 10
'''
t = int(input())  # 테스트 케이스의 수

tree = []

for _ in range(t):
    n = int(input())  # 통나무의 개수
    tree = list(map(int, input().split()))
    tree.sort()
    sorted_tree = [0]*n
    j = 0
    for i in range(0, n//2+n % 2):
        sorted_tree[i] = tree[j]  # 가장 작은 값부터 대입
        if i >= n//2:
            break
        sorted_tree[n-1-i] = tree[j+1]
        j += 2
    level = 0
    for i in range(n):
        if i+1 < n:
            temp = sorted_tree[i+1]-sorted_tree[i]
        else:
            temp = sorted_tree[i] - sorted_tree[0]
        if temp > level:
            level = temp
    print(level)
