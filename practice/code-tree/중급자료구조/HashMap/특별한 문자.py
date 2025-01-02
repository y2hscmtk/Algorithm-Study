str = input()

count = dict()
for i,s in enumerate(str):
    if s in count:
        count[s][0] += 1
    else:
        count[s] = [1,i]

arr = []
for key in count:
    cnt,idx = count[key]
    if cnt == 1: # 한 번만 등장하는 단어 확인
        arr.append((idx,key)) # 가장 먼저 등장하는 단어 확인용

if arr:
    arr.sort()
    print(arr[0][1])
else:
    print("None")