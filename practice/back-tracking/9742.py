# https://www.acmicpc.net/problem/9742

def make_array(idx):
    global find,count
    if find:
        return
    if idx == len(string):
        if count == num:
            result = ''.join(selected)
            print(f'{string} {num} = {result}')
            find = True
        count+=1
        return
    for i in range(len(string)):
        if not visited[i]:
            visited[i] = True
            selected[idx] = string[i]
            make_array(idx+1)
            selected[idx] = 0
            visited[i] = False

while True:
    try:
        string, num = input().split()
        num = int(num)
        visited = [False]*len(string)
        selected = [0]*len(string)
        count = 1
        find = False
        make_array(0)
        if not find:
            print(f'{string} {num} = No permutation')
    except EOFError:
        break