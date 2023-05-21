# https://www.acmicpc.net/problem/2358
'''
하나의 좌표가 일치한다면 => 직선을 그을수 있다.
즉 x,y에 평행하는 한 직선에 대해서, 해당 직선에 포함되는 점이 '2개 이상' 있는지 확인하여
조건을 만족한다면 그 직선을 카운팅한다.
x축에 평행한 직선과 y축에 평행한 직선 둘 다 만족해야하므로
x[] 와 y[] 를 만들어서 좌표별로 몇개씩 있는지 확인한다.
예를 들어 [[0,0],[10,10],[0,10],[10,0]] 의 경우
x[0] = 2, x[10] = 2, y[0] = 2, y[10] = 2 가 되며, 모두 2 이상이므로 4개의 직선이 그어지게 된다.
'''