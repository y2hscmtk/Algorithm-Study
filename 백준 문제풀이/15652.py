# https://www.acmicpc.net/problem/15652

n, m = map(int,input().split())

array = []

# 1 1, 2 2 .. 자기와 같은수에서부터 시작함
def backtracking(count):
    global array
    # m개만큼 수를 찾았다면 출력
    if count == m:
        print(*array)
        return

    for i in range(1,n+1):
        # 가장 마지막 수를 비교하여 같은 수 이상일때만 배열에 삽입
        if len(array) == 0 or i >=array[-1]:
            array.append(i)
            backtracking(count+1)
            array.pop()

backtracking(0)
