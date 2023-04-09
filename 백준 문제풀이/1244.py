# https://www.acmicpc.net/problem/1244
n = int(input())  # 스위치의 개수


# 스위치 상태 변경
def change(i, switch):
    if switch[i] == 0:
        switch[i] = 1
    elif switch[i] == 1:
        switch[i] = 0


def change_switch(gender, number):
    global switch
    if gender == 1:  # 남학생의 경우
        # 남학생은 자기가 받은 숫자의 배수라면 해당 스위치의 상태를 바꾼다
        # 즉 0이라면 1로, 1이라면 0으로 바꾼다
        for i in range(1, n+1):
            if i % number == 0:  # 배수라면
                change(i-1, switch)  # 상태변경
    elif gender == 2:  # 여학생의 경우
        # 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서
        # 가장 많은 스위치를 포함하는 구간을 찾아서,
        # 그 구간에 속한 스위치의 상태를 모두 바꾼다.
        # 만약 좌우가 대칭인 구간이 없다면 해당 번호의 스위치만 바꾼다.
        start, end = number-1, number-1
        while True:
            # 좌우 상태가 대칭이라면
            # 좌우 접근이 가능한 상태인지 확인
            if 0 <= start-1 < n and 0 <= end+1 < n:
                if switch[start-1] == switch[end+1]:
                    start -= 1
                    end += 1
                else:
                    break
            else:
                break  # 일치하지 않는다면 반복 탈출
        for i in range(start, end+1):
            change(i, switch)


switch = list(map(int, input().split()))  # 스위치의 상태
# 학생수 입력받기
sc = int(input())

command = []
for i in range(sc):
    # 성별과 학생이 받은 수를 입력 받는다.
    command.append(map(int, input().split()))


# 입력받은 명령만큼 함수 수행
for gender, number in command:
    change_switch(gender, number)

# 정답 출력은 한줄에 2-개씩
for i in range(n):
    if (i+1) % 20 == 0:
        print(switch[i])
    else:
        print(switch[i], end=" ")
