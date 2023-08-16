# https://www.acmicpc.net/problem/20310

# 1은 뒤쪽에, 0은 앞쪽에 와야함
data = list(input())
zero = data.count('0')
one = data.count('1')

# 1 제거(앞에서 부터 절반)
for i in range(one//2):  # 절반만큼 지우기
    data.pop(data.index('1'))  # 1인값 찾아서 지우기

# 0 제거(뒤에서 부터 절반)
for i in range(zero//2):  # 절반만큼 지우기
    data.pop(len(data)-data[::-1].index('0')-1)  # 1인값 찾아서 지우기
print(''.join(data))
