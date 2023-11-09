# https://www.acmicpc.net/problem/13251
# 조합 nCr을 이용해서 계산
'''
문제
효빈이의 비밀 박스에는 조약돌이 N개 들어있다. 조약돌의 색상은 1부터 M까지 중의 하나이다.
비밀 박스에서 조약돌을 랜덤하게 K개 뽑았을 때, 뽑은 조약돌이 모두 같은 색일 확률을 구하는 프로그램을 작성하시오. 

입력
첫째 줄에 M (1 ≤ M ≤ 50)이 주어진다.
둘째 줄에는 각 색상의 조약돌이 몇 개 있는지 주어진다. 각 색상의 조약돌 개수는 1보다 크거나 같고 50보다 작거나 같은 자연수이다.
셋째 줄에는 K가 주어진다. (1 ≤ K ≤ N)
5
12 2 34 13 17
4
'''
m = int(input())

rocks = list(map(int,input().split()))
# 돌의 전체개수 
n = sum(rocks)
# 뽑아야 하는 돌의 개수
k = int(input())

def nCr(n,r):
    # r이 n의 절반보다 크면, 계산을 간소화하기 위해 r을 n-r로 변경
    r = min(r, n-r)
    '''
    nCr= nx(n-1)x(n-2)×…×(n-r+1) / rx(r-1)x(r-2)x…x1 
    '''
    num,den = 1,1
    for i in range(1,r+1):
        num *= n-r+i # (n-r+1)부터 n에 이르기까지 부분적으로 계산하기 위함
        den = i
        num /= den
    return num

# n개 중에서 K개를 뽑는 경우의 수 => nCk
# 각각의 색에서 K개를 뽑는 경우의 수를 배열을 돌면서 누적시켜서 반환
def pick_rock():
    result = 0
    for rock in rocks:
        # 같은 색 돌을 K개 뽑는 경우의 수
        if rock>=k: # k개보다 많은 경우에 대해서만
            result += nCr(rock,k)
    return result # 전체 경우의 수 반환

# 각각의 같은 색의 돌에서 K개를 뽑는 경우의 수 / 전체(n)개에서 K개를 뽑는 경우의 수
print(pick_rock()/nCr(n,k))

