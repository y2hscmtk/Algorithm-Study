# https://www.acmicpc.net/problem/10989
import sys  # readline()은 더 적은 메모리를 사용한다?
input = sys.stdin.readline
# 메모리 관리를 해야하므로, 매번 배열을 생성하면 메모리 초과가 발생한다.
# 따라서 기존에 미리 최대 입력한계까지 배열을 만들어 둔다.
data = [0] * 10001

# 입력받기
for _ in range(int(input())):
    data[int(input())] += 1 # 입력받은 숫자의 인덱스 만큼 늘려서 표현
# => 위과정을 통해 정렬까지 한번에 처리가 가능하다.

for i in range(10001):
    if data[i] != 0:  # 0이 아니라면, 즉 입력받은 수가 있다면
        for _ in range(data[i]):  # i의 횟수만큼
            print(i)  # 해당 수를 출력해준다. 예를들어 data[1] = 2 이면 1을 2번 출력
