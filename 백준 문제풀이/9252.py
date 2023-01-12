# https://www.acmicpc.net/problem/9252

'''
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 

모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

'''
# 배열 2개 입력받기
arrayA = list(input())
arrayB = list(input())

# LCS를 구하기 위해서는 2차원 배열이 필요
# 두 배열중 크기가 긴 배열의 크기를 SIZE라고 할때, SIZE*SIZE 크기의 2차원배열을 만든다.

# 두 배열의 길이중 더 긴값을 SIZE로 채택
SIZE = len(arrayA) if len(arrayA) > len(arrayB) else len(arrayB)
# 2차원 배열 생성
LCS = [[0]*(SIZE+1) for _ in range(SIZE+1)]

# LCS탐색 알고리즘의 규칙에 따라 2차원 배열에 값 할당
# 한 배열의 값을 대상으로 다른 배열의 값과 비교한다
# 값이 같다면 LCS[i-1][j-1] + 1
# 값이 서로 다르다면 max(LCS[i-1][j],LCS[i][j-1])의 값을 LCS[i][j]에 할당한다.
for i in range(len(arrayA)):
    for j in range(len(arrayB)):
        # 값이 서로 같은 경우
        if arrayA[i] == arrayB[j]:
            # 길이가 늘어난다는 의미
            LCS[j+1][i+1] = LCS[j][i] + 1
        else:
            # 기존의 길이들중 가장 길이가 긴 길이를 채택
            LCS[j+1][i+1] = max(LCS[j][i+1], LCS[j+1][i])

maxLength = 0
# LCS배열에서의 최대값 탐색
for values in LCS:
    # 각 행에서의 최대값을 비교하여 최대값을 maxLength에 저장
    mlength = max(values)
    if maxLength < mlength:
        maxLength = mlength

# LCS의 길이 출력
print(maxLength)

# LCS의 길이가 0이 아닐때만 둘째줄 출력
if maxLength != 0:
    # LCS 문자열 출력용 알고리즘
    # LCS배열의 가장 마지막 값부터 알고리즘 시작
    # LCS[i][j]에서 시작할때, LCS[i-1][j]와 LCS[i][j+1]중 현재값과 같은 값을 찾는다.
    # 같은 값이 존재할경우 해당 자리로 이동해서 위의 과정 반복
    # 같은 값이 존재하지 않는다면 해당 값을 배열에 저장하고 LCS[i-1][j-1]로 이동하여 위의 과정을 반복한다.
    # 배열의 값이 0이라면 알고리즘을 종료하고, 생성한 배열을 역순으로 출력한다.

    # 시작은 가장 마지막 값부터
    i, j = len(arrayB), len(arrayA)
    # 결과를 저장할 배열
    LCSArray = []

    while LCS[i][j] != 0:
        # 배열의 값이 0이라면 알고리즘을 종료한다.
        # if LCS[i][j] == 0:
        #     break
        # 위와 왼쪽의 값중 현재값과 같은값 탐색
        # 일치하면 그곳으로 인덱스 이동
        if LCS[i][j] == LCS[i-1][j]:
            i = i-1
        elif LCS[i][j] == LCS[i][j-1]:
            j = j-1
        # 일치하는 값이 없다면 배열에 값을 저장하고 LCS[i-1][j-1]로 이동
        else:
            LCSArray.append(arrayA[j-1])
            i = i-1
            j = j-1

    # LCS배열 역순으로 만들기
    LCSArray.reverse()

    for data in LCSArray:
        print(data, end='')
