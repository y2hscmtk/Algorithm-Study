# https://www.acmicpc.net/problem/2578
'''
입력
첫째 줄부터 다섯째 줄까지 빙고판에 쓰여진 수가 가장 위 가로줄부터 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 

여섯째 줄부터 열째 줄까지 사회자가 부르는 수가 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 

빙고판에 쓰여진 수와 사회자가 부르는 수는 각각 1부터 25까지의 수가 한 번씩 사용된다.

출력
첫째 줄에 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지 출력한다.
'''
import sys
# 브루트포스로 풀면 될듯?
# 빙고판 입력받기 빙고판은 5x5에 1~25까지의 수가 한개씩 입력됨
board = [list(map(int, input().split())) for _ in range(5)]

# 사용자가 말하는 숫자들 입력받기
speak = [list(map(int, input().split())) for _ in range(5)]


# 빙고 검사 브루트포스
def check():
    count = 0  # 완성한 줄의 개수
    # 가로 빙고 검사
    for i in range(5):
        error = False
        # 맞은 숫자는 0으로 처리됨, 따라서 0이 아닌값이 행의 시작에 존재한다면
        # 그 줄은 더 검사할 필요없음(한줄 전부가 0이어야 하므로)
        if board[i][0] != 0:
            continue  # 다음 행으로 넘어가기
        for j in range(5):
            if board[i][j] != 0:
                error = True
                break  # 가로 줄의 값중, 하나라도 0이 아닌값이 존재한다면 한줄 완성 불가
        # 에러가 발생하지 않았다면 줄 개수 +1
        if not error:
            count += 1
            if count >= 3:
                return True

    # 세로 줄 검사
    for j in range(5):
        error = False
        # 맞은 숫자는 0으로 처리됨, 따라서 0이 아닌값이 열의 시작에 존재한다면
        # 그 줄은 더 검사할 필요없음(한줄 전부가 0이어야 하므로)
        if board[0][j] != 0:
            continue  # 다음 열로 넘어가기
        for i in range(5):
            if board[i][j] != 0:
                error = True
                break  # 하나라도 0이 아닌 값이 존재한다면, 한줄 완성 불가
        # 에러가 발생하지 않았다면 줄 개수 +1
        if not error:
            count += 1
            if count >= 3:
                return True

    # 오른쪽 대각선 검사
    error = False
    for i in range(5):
        if board[i][i] != 0:
            error = True
            break
    if not error:
        count += 1
        if count >= 3:
            return True
    # 왼쪽 대각선 검사
    error = False
    for i in range(5):
        if board[i][4-i] != 0:
            error = True
            break
    if not error:
        count += 1
        if count >= 3:
            return True
    # 빙고 완성 못했으면 False 리턴
    return False


count = 0
# 빙고가 완성되려면 최소 12개 이상의 숫자가 외쳐진 후여야 하므로, 12개 숫자 이후부터 검사하기
for i in range(5):
    for j in range(5):
        number = speak[i][j]
        found = False
        for x in range(5):
            if found:
                break
            for y in range(5):
                if number == board[x][y]:
                    board[x][y] = 0
                    count += 1
                    found = True  # 찾았음으로 표시
                if found:
                    if count >= 12:
                        if check() == True:
                            print(count)
                            sys.exit(0)
                    break  # 해당 반복 종료
print(count)
