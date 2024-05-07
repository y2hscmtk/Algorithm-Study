# https://www.acmicpc.net/problem/28454
data = input()
gift,result = [],0
for _ in range(int(input())):
    gift.append(input())
for g in sorted(gift):
    if g >= data:
        result += 1
print(result)