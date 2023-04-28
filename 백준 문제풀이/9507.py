# https://www.acmicpc.net/problem/9507

# 메모이제이션 이용
# n은 최대 67

'''
n < 2 :                         1
n = 2 :                         2
n = 3 :                         4
n > 3 : koong(n − 1) + koong(n − 2) + koong(n − 3) + koong(n − 4)
'''
koong = [[] for _ in range(68)]
koong[0], koong[1] = 1, 1
koong[2] = 2
koong[3] = 4
for n in range(4, 68):
    koong[n] = koong[n-1] + koong[n-2] + koong[n-3] + koong[n-4]

for i in range(int(input())):
    print(koong[int(input())])
