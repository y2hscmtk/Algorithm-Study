# https://www.acmicpc.net/problem/1331
# 모든칸을 정확히 한번씩 방문
# 이동은 '나이트'의 움직임
# 주어진 좌표에서 중복으로 등장하는 좌표가 없으며
# 다음에 이동할 좌표가 '나이트'로서 이동 가능한 경로이며
# 마지막 좌표에서 A1으로 되돌아 올 수 있는 지(나이트로서) 확인
# 모든 조건을 만족한다면 Valid, 만족하지 않는다면 Invalid
dx = [0, -1, -2, -2, -1, 1, 2, 2, 1]
dy = [0, -2, -1, 1, 2, 2, 1, -1, -2]
# 나이트의 움직임 입력받기
moves = [input() for _ in range(36)]
# # 나이트 투어를 시작하는 위치 길고
start_x = ord(moves[0][0]) - ord('A')
start_y = int(moves[0][1])-1
# 이동 정보를 저장하기 위한 배열 생성
visited = [[False]*6 for _ in range(6)]


# 올바른 경로인지 확인
# 방문한적 없는 좌표만 방문해야한다.
# 모든 칸을 한번씩 방문해야 한다.
def is_correct():
    curr_x, curr_y = start_x, start_y  # 현재 좌표
    for move in (moves):
        # 배열에 적합한 좌표로 변환
        nx = ord(move[0]) - ord('A')  # 좌표로 변환
        ny = int(move[1]) - 1
        if not visited[nx][ny]:  # 방문한적 없다면
            # 현재 위치에서 나이트의 움직임으로 방문이 가능한지 확인
            able = False
            for j in range(len(dx)):
                if (nx, ny) == (curr_x + dx[j], curr_y + dy[j]):
                    able = True  # 가능한 경로임
                    break
            if able:  # 나이트의 움직임으로도 이동 가능한 경로라면 방문처리
                visited[nx][ny] = True  # 방문처리
                curr_x, curr_y = nx, ny  # 현재 위치 갱신
        else:  # 만약 방문한적 있는 좌표에 다시 방문한다면
            return False  # 올바르지 않은 좌표임
    # 마지막 좌표까지 다 돌았다면 시작위치로 다시 되돌아 올 수 있는지 확인
    able = False
    for i in range(len(dx)):
        if (start_x, start_y) == (curr_x + dx[i], curr_y + dy[i]):
            able = True  # 시작 위치로 되돌아 올 수 있음
    # 모든 좌표를 다 방문했는지도 검사
    if able:
        for array in visited:
            if False in array:
                return False
        return True
    else:
        # 시작 위치로 되돌아 올 수 없다면
        return False


# 올바른 경로면 Valid, 올바르지 않은 경로면 Invalid
print("Valid") if is_correct() else print("Invalid")
