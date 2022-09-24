# 어느 날, 미르코는 우연히 길거리에서 양수 N을 보았다. 미르코는 30이란 수를 존경하기 때문에,
# 그는 길거리에서 찾은 수에 포함된 숫자들을 섞어 30의 배수가 되는 가장 큰 수를 만들고 싶어한다.
# 미르코를 도와 그가 만들고 싶어하는 수를 계산하는 프로그램을 작성하라.
from itertools import *  # 순열을 사용하기 위한 라이브러리

n = input()

# 아이디어
# 먼저 각 자리수를 바꿔가면서 만들 수 있는 모든 수를 만들어 배열에 저장하고,
# 그 배열을 내림차순으로 정렬한 뒤, 배열에서 수를 하나씩 뽑으면서 해당 숫자가 30의 배우인지 확인후 출력한다.
# 배열을 모두 탐색하고도 30의 배수가 없으면 -1 출력

data = list(permutations(n, len(n)))  # n에서 모든 요소의 위치를 바꿔가며 만들수 있는 모든 경우의 수를 만듦
num_data = []

for i in range(len(data)):
    num = ''.join(data[i])
    if int(num) % 30 == 0:
        num_data.append(int(num))

num_data.sort(reverse=True)  # 내림차순 정렬

check = False
for i in num_data:
    if i % 30 == 0:
        print(i)
        check = True
        break

if check == False:
    print(-1)
