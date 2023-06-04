# https://www.acmicpc.net/problem/3040
from itertools import combinations

# 브루트포스
# 더해서 100이 되는 수를 출력 => 조합 이용
n = []
for _ in range(9):
    n.append(int(input())) # 각 난쟁이 키 입력받아 저장

# 난쟁이들 중에서 7명 뽑아서 키 더해보고, 100되면 출력
for array in combinations(n,7):
    if sum(array) == 100:
        print(*array, sep='\n') # 100이 된다면 키 하나씩 출력
