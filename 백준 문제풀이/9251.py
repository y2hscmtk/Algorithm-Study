# https://www.acmicpc.net/problem/9251

'''
LCS(Longest Common Subsequence, 

최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 

모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

'''

'''
최장 공통 부분 수열 알고리즘은 다음 블로그의 이론을 참고하였다.
https://velog.io/@emplam27/알고리즘-그림으로-알아보는-LCS-알고리즘-Longest-Common-Substring와-Longest-Common-Subsequence
'''


# 배열 2개 입력받기
arrayA = list(input())
arrayB = list(input())

# 두 배열중 더 긴 배열을 기준으로 2차원 배열 LCS 만들기

# 두 배열의 길이중 더 긴 배열을 대상으로 2차원 배열 생성
SIZE = len(arrayA) if len(arrayA) > len(arrayB) else len(arrayB)

SIZE += 1

# SIZE x SIZE 크기의 2차원 배열 생성
LCS = [[0]*SIZE for _ in range(SIZE)]

# 배열 a,b의 인덱스를 차래로 늘려주기 위해?
index_a = 0
index_b = 0
# 알고리즘 적용
# 두 배열의 값을 비교하여 LCS알고리즘에 맞춰 LCS 배열에 값을 할당한다.
for i in range(len(arrayA)):
    for j in range(len(arrayB)):
        # 같은 값을 발견하였다면 LCS[i-1][j+1]+1의 값으로 초기화
        if arrayA[i] == arrayB[j]:
            LCS[i+1][j+1] = LCS[i][j] + 1
        # 같은 값이 아니라면 LCS[i-1][j] 와 LCS[i][j-1] 둘 중에 큰 값으로 값을 정한다.
        else:
            LCS[i+1][j+1] = max(LCS[i][j+1], LCS[i+1][j])

# 가장 긴 길이 결정
maxLength = LCS[0][0]

for data in LCS:
    # 임시 최대 길이
    mLength = max(data)
    if maxLength < mLength:
        maxLength = mLength

# 최장 부분 수열의 길이 출력
print(maxLength)
