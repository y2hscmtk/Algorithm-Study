# https://www.acmicpc.net/problem/14500
from collections import deque

# 각 테트로미노에 대한 방향벡터 정의
block = [
# ---- 블록(가로로 3칸 이동)
[[0,0,0],[1,2,3]]
# 세로 일자 블록
[[1,2,3],[0,0,0]]
# 네모 블록
[[0,1,1],[1,0,0]]
# L블록
[[],[]]
# J블록

# ㅣ-블록

# 7블록

# 

#

#

#

# ㅜ 블록

# ㅗ 블록

# ㅓ 블록

# ㅏ 블록

]




n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]


# 각 모양에 대해 브루트포스
