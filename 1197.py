# https://www.acmicpc.net/problem/1197

'''
첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다.

다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다.

이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다.

C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.

그래프의 정점은 1번부터 V번까지 번호가 매겨져 있고, 임의의 두 정점 사이에 경로가 있다.

최소 스패닝 트리의 가중치가 -2,147,483,648보다 크거나 같고,

2,147,483,647보다 작거나 같은 데이터만 입력으로 주어진다.
'''
v, e = map(int, input().split())  # v 정점의 개수, e 간선의 개수

# 가중치가 0으로 초기화된 2차원 행렬을 생성

adj_mat = [[] for _ in range(v)]

# for i in range(v):
#    adj_mat.append(['x']*v)  # x는 해당경로로 갈수 없음을 의미

for _ in range(e):  # 간선의 개수만큼 반복하며 가중치 입력받음
    start, end, weight = map(int, input().split())  # 입력받은 가중치 입력
    adj_mat[start-1].append([weight, end-1])  # 문제에서는 시작정점이 1부터이므로
    adj_mat[end-1].append([weight, start-1])


# MST 알고리즘 시작
sum = 0  # 가중치를 저장할 변수공간

# 프림 알고리즘으로 구현
select = [0]  # 방문처리


# def get_min_vertix(adj_mat, select, v):
#     min_weight = 2147483648
#     for s in select:  # select안의 정점들을 하나씩 꺼내서 인접정점 파악
#         for e in adj_mat[s]:
#             if e[1] in select:  # 해당 정점이 이미 방문됐다면
#                 continue
#             if e[0] < min_weight:
#                 min_weight = e[0]
#                 min_vertix = e[1]
#     return min_vertix, min_weight
# for i in range(v):
#     if adj_mat[s][i] == 'x' or i in select:  # 선택한 정점으로의 길은 고려하지않음
#         continue  # 해당경로로는 갈수 없음을 의미
#     if adj_mat[s][i] < min_weight:
#         min_weight = adj_mat[s][i]
#         min_vertix = i
# return min_vertix, min_weight  # 최소 정점과 그 간선 리턴


count = 1
while count < v:
    # 최소간선을 갖는 정점 찾기
    min_weight = 2147483648
    for s in select:  # select안의 정점들을 하나씩 꺼내서 인접정점 파악
        for e in adj_mat[s]:
            if e[1] in select:  # 해당 정점이 이미 방문됐다면
                continue
            if e[0] < min_weight:
                min_weight = e[0]
                min_vertix = e[1]
    #min_vertix, min_weight = get_min_vertix(adj_mat, select, v)
    select.append(min_vertix)  # 해당 정점 방문처리
    count += 1
    sum += min_weight  # 비용 누적

print(sum)
