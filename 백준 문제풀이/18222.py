# https://www.acmicpc.net/problem/18222
'''
k는 10^18 => 직접 수를 만든다면 시간초과

1. X는 맨 처음에 "0"으로 시작한다. 
2. X에서 0을 1로, 1을 0으로 뒤바꾼 문자열 X'을 만든다.
3. X의 뒤에 X'를 붙인 문자열을 X로 다시 정의한다. 
4. 2~3의 과정을 무한히 반복한다.

조건 3에 의해, 2배씩 늘어난다는 점을 알 수 있다.

<아이디어>
가장 가까운 2의 거듭제곱 찾기
'''
k = int(input())
# k보다 작은 2의 거듭제곱 반환
def findPower():
    n = 1; count = 0
    while True:
        if n >= k:
            return n//2
        n *= 2; count += 1
        
# 현재 수보다 작은 2의 거듭 제곱을 찾아서 현재 수에서 빼준다.
# 위 과정을 1이 될 때 까지 반복
# 짝수번에 왔다면 => 수가 바뀌지 않음 => 0
# 홀수번에 왔다면 => 수가 바뀜 => 1(시작 숫자는 0)
count = 0
while True:
    if k == 1:
        if count%2 == 0:
            print(0)
        else:
            print(1)
        break
    k -= findPower()
    count+=1