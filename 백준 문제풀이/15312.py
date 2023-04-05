# https://www.acmicpc.net/problem/15312
change = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 3, 'F': 3, 'G': 2,
          'H': 3, 'I': 3, 'J': 2, 'K': 2, 'L': 1, "M": 2, 'N': 2, 'O': 1,
          'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1, 'V': 1, 'W': 1,
          'X': 2, 'Y': 2, 'Z': 1}

A = input()
B = input()

temp = []
# 먼저 문자를 모두 숫자로 변환하여 배열에 삽입
for i in range(len(A)):
    temp.append(change[A[i]])
    temp.append(change[B[i]])

index = len(A)
length = index*2

while True:
    # 두 글자를 이어붙여 만든 길이가 2글자라면 반복 종료
    if length == 2:
        print(str(temp[0])+str(temp[1]))
        break
    j = 0
    for i in range(length-1):
        temp[j] = (temp[i] + temp[i+1]) % 10
        j += 1
    length -= 1
