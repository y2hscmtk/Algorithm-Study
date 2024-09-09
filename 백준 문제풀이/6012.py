# https://www.acmicpc.net/problem/6012
'''
1     2     3     4     5     6  |  7     8     9     10     11
    1     2     3  |  4     5     6
        1     2  |  3
                1  2        => 1*2=2 added to sum -> sum=2
                3           => sent home with rose
        4     5  |  6
                4  5        => 4*5=20 added to sum -> sum=22
                6           => sent home with rose
    7     8     9  | 10    11
        7     8  |  9
                7  8        => 7*8=56 added to sum -> sum=78
                9           => sent home with rose
        10    11            => 10*11=110 added to sum -> sum=188
세수 이하가 될때, 앞에서 2개의 수를 곱해서 정답에 더한다.
이후 완성된 정답을 출력한다.
'''
N = int(input())
numbers = [i for i in range(1,N+2)]
def recursion(s, e):
    global result
    size = e - s + 1
    if size == 2:  # 두 마리의 소가 있으면 곱해서 더함
        result += numbers[s] * numbers[e]
        return
    elif size == 1:  # 한 마리의 소는 장미를 받고 집으로 감
        return
    # 중간 지점 찾기
    mid = (s + e) // 2
    recursion(s, mid)
    recursion(mid + 1, e)
result = 0 # 정답
recursion(0, N - 1)
print(result)
