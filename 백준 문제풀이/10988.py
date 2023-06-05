# https://www.acmicpc.net/problem/10988

data = input()
size = len(data)
error = False
for i in range(size//2):
    if data[i] == data[size-i-1]:
        continue
    else:
        error = True
        break
print(0) if error else print(1)
