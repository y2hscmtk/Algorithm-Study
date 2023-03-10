'''
왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기가 찾아왔다.

일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명이었던 것이다.

아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고 주장했다. 

뛰어난 수학적 직관력을 가지고 있던 백설공주는,

다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.

아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.
'''
from itertools import combinations

# 9개의 줄에 걸쳐서 키를 입력받는다.
data = []
for i in range(9):
    data.append(int(input()))

# 난쟁이들의 키를 대상으로 탐색을 진행하여 숫자 100이 완성되었으면,
# 난쟁이들의 키를 오름차순으로 출력한다.

result = []  # 정답을 저장할 배열

# 조합을 이용하여 7명의 난쟁이의 키들을 기록한다.
for random_data in combinations(data, 7):
    # 난쟁이들의 키의 합이 100이라면 반복 종료
    if sum(random_data) == 100:
        result = list(random_data)
        break  # 반복 종료

result.sort()  # 오름차순 정렬

# 한줄에 데이터 한개씩 출력
for hegiht in result:
    print(hegiht)
