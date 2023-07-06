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
                    ↑ if lf==n && rf==n; print(count); break;
'''