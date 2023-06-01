'''

time = 2
2,1
5,7
8,3
일때
time+1보다 다음사람이 들어오는 시간이 큼
=> time = 5
time+7보다 8이 작음
=> time +=7 += 3(8인 사람이 걸리는 시간)
'''

# 먼저 데이터를 입력받고 들어오는 순으로 재정렬
n = int(input())
data = []
for _  in range(n):
    start,end = map(int,input().split())
    data.append([start,end])

data.sort() # 들어온 시간을 기준으로 재정렬

# 초기 time값은 첫번째 사람의 업무 처리 시간
time = sum(data[0])
if len(data)==1: # 한사람이라면
    print(time)
else:
    for i in range(1,len(data)):
        start,end = data[i]
        if time <= start:
            time = start+end
        else:
            time+=end

    print(time)
