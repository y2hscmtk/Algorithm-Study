# https://www.acmicpc.net/problem/10809

words = list(input())
# 알파벳 위치를 저장할 배열
check = [-1]*26
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(words)):
    index = alphabet.index(words[i])
    if check[index] == -1: # 아직 기록이 안된 경우에만
        check[index] = i

# 정답 출력
print(*check)
