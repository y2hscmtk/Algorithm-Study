# https://www.acmicpc.net/problem/2018
'''
아이디어 : 투포인터
lf와 rf를 이용
<Algorithm>
n = 10
if sum[lf:rf+1] < 10; rf++ (더 더할 수 있음) 
else if sum[lf:rf+1] == 10; count++ rf++
else lf++ //sum[lf:rf+1] > 10인 경우, 너무 많이 더했으므로, 덜 더해야함

(example)
1 2 3 4 5 6 7 8 9 10
↑ lf
↑ rf

1 2 3 4 5 6 7 8 9 10
↑ ↑ ; sum[1:2+1] < 10; rf++

...

1 2 3 4 5 6 7 8 9 10
↑     ↑ ; sum[1:5] == 10; count++, rf++

1 2 3 4 5 6 7 8 9 10
↑       ↑ ; sum[1:5] > 10; lf++

1 2 3 4 5 6 7 8 9 10
  ↑       ↑ ; sum[1:5] > 10; lf++
...

1 2 3 4 5 6 7 8  9 10
                    ↑
                    ↑ if rf==n; print(count); break;
'''
count = 0 # 만들 수 있는 경우의 수 (정답)
n = int(input())
data = [i for i in range(1,n+1)]
lf,rf = 0,0 # 포인터의 초기 위치 0

while True:
    if rf==n:
        break 
    temp = sum(data[lf:rf+1])
    if temp == n:
        count+=1
        rf+=1
    elif temp < n:
        rf+=1
    elif temp > n:
        lf+=1

print(count)