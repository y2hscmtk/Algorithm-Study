n,x = map(int,input().split())
voice = list(map(int,input().split()))
i = 0 # 시작 번호
while True:
    # 상한선보다 내야하는 목소리가 높다면
    if x > voice[i]:
        print(i+1)
        break
    x+=1 # 목소리 낼 수 있으면 다음사람은 더 높은 목소리
    i+=1
    i%=n # 모듈러 연산
