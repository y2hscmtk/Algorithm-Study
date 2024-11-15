'''
p에 멈춰서지 않아야함
N은 1부터 시작하여 차레로 올라가므로, n(n-1)/2가 p이상인 경우 첫번째(N=1)일때 움직이지 않음으로서 p-1에 무조건 도달할 수 있음
n(n-1)/2가 p보다 작은 경우 합이 정답
n(n-1)/2가 p와 같은 경우 p-1이 정답
n(n-1)/2가 p보다 크고, 올라가는 도중
p에 도달해야 한다면 p-1에 도달한 뒤 이동 -> n(n-1)/2 - 1
p에 도달하지 않는다면 n(n-1)/2
'''
t = int(input())
for _ in range(t):
    n,p = map(int,input().split()) 
    floor = 0
    for i in range(1,n+1):
        floor += i
        if floor == p:
            floor -= 1
    print(floor)
        
            
