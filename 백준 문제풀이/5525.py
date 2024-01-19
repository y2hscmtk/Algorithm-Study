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

def isCorrect(i):
    global result
    # Pn의 길이를 모두 검사할수 있는지 검사
    # (배열의 영역을 벗어나지는 않는지)
    if i + len(pn) > m:
        return False
    if s[i:i+len(pn)] == pn:
        result += 1
        return True
    return False


i = 0
while i < m:
    # I 발견시, 패턴 검사
    if s[i] == 'I' and isCorrect(i):
        i += 2 # 패턴과 일치한다면 다음으로 이동
        continue
    i+=1 # I가 아니라면 다음 문자로 이동

print(result)