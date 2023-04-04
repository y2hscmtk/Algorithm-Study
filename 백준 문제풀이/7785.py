# https://www.acmicpc.net/problem/7785
'''
4
Baha enter
Askar enter
Baha leave
Artem enter
'''
n = int(input())
array = []
for _ in range(n):
    p, c = input().split()
    if c == 'enter':
        array.append(p)
    elif c == 'leave':
        array.remove(p)

# 사전순의 역순으로
array.sort(reverse=True)

for people in array:
    print(people)
