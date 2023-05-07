# https://www.acmicpc.net/problem/11637
'''
각 테스트 케이스는 첫 번째 줄부터 순서대로 출력된다. 
최다 득표자가 과반수 득표를 했을경우에는 "majority winner R",
절반 이하의 득표를 하였을 경우엔 "minority winner R"가 되며, 
최다 득표자가 없을때(최다 득표자가 1명 초과일 경우)  "no winner"를 출력한다. 
이때 R은 최다 득표자의 후보자 번호를 의미하며, 후보자의 번호는 각 케이스에서 1, 2, . . . , n 으로 부여된다.
'''
for _ in range(int(input())):
    point = []
    n = int(input())
    # 사람 수만큼 반복
    for _ in range(n):
        # 점수 입력받기
        point.append(int(input()))
    total = sum(point)  # 총 점수 확인
    # 가장 점수 높은 사람 파악
    winner = point.index(max(point)) + 1

    # 최다 득표자가 1명 초과인지 확인
    if point.count(max(point)) > 1:
        print("no winner")
        continue

    # 과반수 득표인지 확인
    if max(point) > total/2:
        print(f"majority winner {winner}")
    else:
        print(f"minority winner {winner}")
