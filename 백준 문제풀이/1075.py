# https://www.acmicpc.net/problem/1075
n = input()
f = int(input())
# 뒷자리 2개를 자른후 00부터 99까지 모든 결과를 시행해봄
start = int(n[:-2] + "00")
end = int(n[:-2] + "99")
for num in range(start,end+1,1):
    # 나누어 떨어지는지 확인
    if num%f==0:
        s = str(num)[-2:]
        print(s)
        break
        # 나누어 떨어지면 종료 => 00부터이므로 당연히 최소값임