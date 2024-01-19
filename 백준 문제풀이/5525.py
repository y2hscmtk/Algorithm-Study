# https://www.acmicpc.net/problem/5525
'''
I를 만나면 Pn인지 검사하고, 일치한다면 2글자 다음으로 이동하여 반복
2글자 다음으로 이동하는 이유는 IOI의 끝 I부터 동일한 패턴이 반복 될 수 있으므로

=> IOI를 굳이 미리 만들 필요가 없다.
=> I 발견시 IOI인지 확인하고 IOI라면 +2해서 다음 칸으로 이동하여 다시 IOI인지 검사한다.
=> IOI가 아니게 되는 시점까지 발견된 IOI의 개수를 검사하고 n개인지 확인하면 된다
'''
n = int(input())
m = int(input())
s = input()
result = 0

i,count = 0,0
while i+3<=m:
    if s[i:i+3] == 'IOI':
        count += 1 # IOI개수 +1
        i+=2 # 2칸 다음으로 이동(다음 I)        
        # n개를 찾았는지 확인
        if count == n:
            result += 1
            count -= 1 # 1 감소(다음시점에서 현재 IOI만 취급x)
    else: # 발견 실패시 => 끊어짐
        i+=1 # 다음 문자로 이동하여 검사
        count = 0 # 끊어졌으므로 초기화


print(result)