# https://www.acmicpc.net/problem/2437

# 하나의 양팔 저울을 이용하여 물건의 무게를 측정하려고 한다. 이 저울의 양 팔의 끝에는 물건이나 추를 올려놓는 접시가 달려 있고, 양팔의 길이는 같다.

# 또한, 저울의 한쪽에는 저울추들만 놓을 수 있고, 다른 쪽에는 무게를 측정하려는 물건만 올려놓을 수 있다.

# 무게가 양의 정수인 N개의 저울추가 주어질 때, 이 추들을 사용하여 측정할 수 없는 양의 정수 무게 중 최솟값을 구하는 프로그램을 작성하시오.

# 예를 들어, 무게가 각각 3, 1, 6, 2, 7, 30, 1인 7개의 저울추가 주어졌을 때, 이 추들로 측정할 수 없는 양의 정수 무게 중 최솟값은 21이다.

n = int(input())

# 공백으로 구분하여, 저울추들의 무게 입력받기
w = list(map(int, input().split()))

# 아이디어 : 무게추를 오름차순으로 정렬시킨 후, 1부터 sum(w)까지의 수를 무게추의 무게를 조합하여 만들 수 있는지 파악하면 됨

w.sort()  # 오름차순 정렬

start, end = 0, 0
mstart, mend = 0, 0
result = 0

for i in w:
    mstart = start + i
    mend = end + i
    if (mstart <= end) or (mstart-end == 1):  # 새로운 무게추가 추가되었을때, 연결이 되어있는지 아닌지를 확인
        start = 0
        end = mend
        mstart, mend = 0, 0
    else:
        result = end + 1
        break

if result == 0:
    print(end+1)
else:
    print(result)
