# https://www.acmicpc.net/problem/18222

# 초기에 x는 0으로 시작한다.
x = '0'

# x'을 만들어서 x에 붙이는 함수
def make():
    global x
    y = ""
    for i in range(len(x)):
        y += str(abs(int(x[i])-1))

    x += y

'''
입력된 수를 보고, 재귀함수를 호출할 횟수 결정
1번의 수행으로 수는 기존길이**2의 길이가됨
입력된 수보다 작은 2의 배수만큼 계산을 수행
입력된 수 : 9 => 3번 수행

'''
start = 1
count = 0
n = int(input())
while True:
    if start<n:
        start*=2
        count+=1
    else:
        # 해당길이를 만들수 있을만큼 함수호출
        for i in range(count):
            make()
        break
    
print(x[n-1])