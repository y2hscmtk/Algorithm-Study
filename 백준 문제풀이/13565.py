# https://www.acmicpc.net/problem/13565

'''
인제대학교 생화학연구실에 재직중인 석교수는 전류가 침투(percolate) 할 수 있는 섬유 물질을 개발하고 있다. 

이 섬유 물질은 2차원 M × N 격자로 표현될 수 있다. 편의상 2차원 격자의 위쪽을 바깥쪽(outer side), 아래쪽을 안쪽(inner side)라고 생각하기로 한다. 

또한 각 격자는 검은색 아니면 흰색인데, 검은색은 전류를 차단하는 물질임을 뜻하고 흰색은 전류가 통할 수 있는 물질임을 뜻한다. 

전류는 섬유 물질의 가장 바깥쪽 흰색 격자들에 공급되고, 이후에는 상하좌우로 인접한 흰색 격자들로 전달될 수 있다.

김 교수가 개발한 섬유 물질을 나타내는 정보가 2차원 격자 형태로 주어질 때, 

바깥쪽에서 흘려 준 전류가 안쪽까지 침투될 수 있는지 아닌지를 판단하는 프로그램을 작성하시오.
'''
'''
아래쪽까지 도달하는것이 목표이므로, BFS를 실시하여 가장 바닥까지 도달하였다면 탐색을 중단한다.
맨 윗줄에서 0인 좌표를 대상으로 bfs를 진행하고 만약 맨 윗줄에 0인 좌표가 없다면 전기가 통할수 없으므로 BFS없이 NO 출력
'''
from collections import deque
m, n = map(int, input().split())

graph = [list(input()) for _ in range(m)]


def bfs(s, e):
    queue = deque([s, e])
