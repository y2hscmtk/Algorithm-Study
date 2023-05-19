# https://www.acmicpc.net/problem/27514
n = int(input())
data = list(map(int,input().split()))
maxNum = max(data)
dict = {0:0}
i = 1 # 1을 고려하지 않았네..
while i!=2*maxNum:
    dict[i] = 0
    i *= 2
for num in data:
    dict[num] += 1 # 추가

# #print(dict)
# 딕셔너리 압축하기
for key in dict:
    if key==0: # 0인 경우는 무시
        continue
    count = dict[key] # 해당 수가 몇개인지
    # 현재 키에서 2배를 한값이, 가장 큰 수의 4배값이라면 
    # => 마지막까지 압축을 마쳤다는 의미가 됨
    if key*2 == 4**maxNum:
        break
    # count//2개만큼의 다음수가 생김
    if key**2 not in dict:
        dict[key*2] = count//2
    else:
        dict[key*2] += (count//2)

for key,item in sorted(dict.items(), reverse=True):
    if item!=0:
        print(key)
        break