# https://www.acmicpc.net/problem/15663
'''
백트래킹 연습, 중복은 visited 생각할것
'''
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
visited = [False]*n
numbers.sort()  # 오름차순 출력을 위해
array = []


def backtracking(count):
    global array, visited
    if count == m:  # m개 뽑았으면
        # last = array[-1]  # 마지막 수 기록
        print(*array)
        return
    last = -1
    for i in range(n):
        # 아직 사용하지 않은 값이라면
        # 같은 인덱스의 값은 더이상 사용하지 말아야하고 마지막 수를 비교하여 같은 출력이 없도록 해야함
        if not visited[i] and numbers[i] != last:
            # '마지막 수'를 비교하여 같은 출력이 없도록 해야함
            visited[i] = True  # 방문처리
            array.append(numbers[i])
            last = numbers[i]  # 마지막으로 사용한 수 기록
            backtracking(count+1)
            array.pop()
            visited[i] = False


backtracking(0)
