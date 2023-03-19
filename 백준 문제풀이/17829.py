# https://www.acmicpc.net/problem/17829
'''
222-풀링은 각 정사각형에서 2번째로 큰 값을 남겨, 새로운 배열을 만드는 연산을 의미한다.
종욱이는 N×N 행렬에 222-풀링을 반복해서 적용하여 크기를 1×1로 만들었을 때 어떤 값이 남아있을지 궁금해한다.

입력

첫째 줄에 N(2 ≤ N ≤ 1024)이 주어진다. N은 항상 2의 거듭제곱 꼴이다. (N=2K, 1 ≤ K ≤ 10)

다음 N개의 줄마다 각 행의 원소 N개가 차례대로 주어진다. 행렬의 모든 성분은 -10,000 이상 10,000 이하의 정수이다. 

출력

마지막에 남은 수를 출력한다.
'''
n = int(input())

# 배열 입력받기
array = [list(map(int, input().split())) for _ in range(n)]


# 222풀링 함수 정의
# 배열을 매개변수로 받아서, 새로운 배열을 만들어 리턴
def tttpooling(array):
    global n  # 배열의 사이즈 n*n
    # 새로운 배열 생성
    new_array = [[0]*(n//2) for _ in range(n//2)]

    # 풀링 작업 수행
    for i in range(0, n, +2):
        for j in range(0, n, +2):
            # 네가지 수들중 두번째로 큰 수 찾기
            sorted_data = [array[i][j], array[i+1][j],
                           array[i][j+1], array[i+1][j+1]]
            sorted_data.sort(reverse=True)  # 내림차순으로
            new_array[i//2][j//2] = sorted_data[1]

    n //= 2  # n의 크기 줄이기
    return new_array


# 숫자가 한개 남을때까지 풀링함수를 반복한다.
while True:
    if len(array) == 1:
        print(*array[0])
        break
    array = tttpooling(array)
