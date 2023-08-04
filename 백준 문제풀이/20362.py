from collections import defaultdict
dict = defaultdict(int) # 정답이 몇번 나왔는지 저장하기 위함
N,S = input().split()
result = 0
for _ in range(int(N)):
    name,log = input().split()
    if name==S:
        result = dict[log]
    dict[log]+=1
print(result)
