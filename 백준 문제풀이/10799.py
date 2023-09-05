# https://www.acmicpc.net/problem/10799
'''
한 막대의 시작과 끝 사이에 레이저가 몇개 있는지 확인
1 + 레이저 한 값이 그 막대가 나눠진 결과 생성된 막대의 개수임
따라서 각 막대의 시작과 끝을 파악하고 [')' 을 만났을때 이전에 '('이 아니라면 가장 인접한 '('을 사용처리]
그 구간내에 ()가 몇개 있는지 확인하여 구간별 막대수를 정답에 더하면 됨
'''
stick = input()

postion = []  # 왼쪽 괄호의 위치를 저장하기 위함
result = 0  # 나눠진 막대의 수
for i in range(len(stick)):  # 끝이 (로 끝나는 경우는 없으므로 인덱스 초과 위험 없음
    if stick[i] == '(':  # 왼쪽 괄호 만나면 인덱스 스택에 푸쉬
        # 다음 문자열과 비교하여 다음 문자열도 (이라면 스택에 푸쉬
        if stick[i+1] == '(':
            postion.append(i)
    else:  # 오른쪽 괄호를 만난경우
        if stick[i-1] == '(':  # 레이저라면 넘어가기
            continue
        else:  # 레이저가 아니라면, 즉 막대의 끝이라면
            j = postion.pop()  # 막대의 시작 인덱스 받아오기
            laser = 0
            meet = False  # (만났을때, 이전에 )였는지 확인
            for k in range(i, j, -1):
                # 범위를 벗어나지 않으면서 )를 만났을때 다음값이 (인지 확인
                # (())())
                if stick[k] == ')':
                    meet = True
                else:
                    if meet:
                        laser += 1
                        meet = False
            result += (laser+1)
print(result)
