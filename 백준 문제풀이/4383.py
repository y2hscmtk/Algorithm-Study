# https://www.acmicpc.net/problem/4383
'''
길이가 1인 수열은 무조건 Jolly jumper이고,
길이가 2이상일 때는 n개의 연속된 두 수의 차의 절댓값이 1부터 n-1까지 모두 나와야 Jolly jumper라고 한다.
케이스마다 Jolly jumper인지를 판별하자.
'''
while True:
    try:
        data = list(map(int,input().split()))
        n,array = data[0],data[1:]
        if n == 1:  # 길이가 1인 수열은 무조건 Jolly
            print("Jolly")
            continue
        # 1 ~ (n-1)까지의 수가 모두 나와야한다.
        visited = [False]*(n)
        visited[0] = True
        for i in range(len(array)-1):
            index = abs(array[i]-array[i+1])
            if 0<=index<n:
                visited[index] = True
        if visited.count(False) >= 1:
            print("Not jolly")
        else:
            print("Jolly")
    except:
        break