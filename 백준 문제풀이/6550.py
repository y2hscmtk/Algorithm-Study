# https://www.acmicpc.net/problem/6550
# 입력이 더이상 없을때까지 반복해야하므로 try-catch활용

while True:
    try:
        s, t = input().split()
        i = 0 # S문자열의 인덱스를 가리키기 위함
        for j in range(len(t)):
            if t[j] == s[i]:
                i += 1
            if i == len(s): # 원하는 단어를 찾았으면 이후 탐색x
                break
        # 단어를 찾았으면 Yes출력, 아니면 No출력
        print("Yes") if i == len(s) else print("No")
    # 더이상 입력이 없다면 종료,
    except EOFError:
        break
