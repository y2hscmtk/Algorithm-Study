# 민식이는 수학학원에서 단어 수학 문제를 푸는 숙제를 받았다.

# 단어 수학 문제는 N개의 단어로 이루어져 있으며, 각 단어는 알파벳 대문자로만 이루어져 있다. 이때, 각 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제이다. 같은 알파벳은 같은 숫자로 바꿔야 하며, 두 개 이상의 알파벳이 같은 숫자로 바뀌어지면 안 된다.

# 예를 들어, GCF + ACDEB를 계산한다고 할 때, A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7로 결정한다면, 두 수의 합은 99437이 되어서 최대가 될 것이다.

# N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성하시오.

# 아이디어 : 같은 자리수가 되기 전까지 9부터 차례로 값을 대입, 같은 자리수부터는 단어의 길이가 긴 단어부터 차례로 값을 대입한다.
# => 실패

# 아이디어2 : 수학으로 접근

# BCD
# ABC
# => 100B + 10C + D + 100A + 10B + C => 110B + 100A + 11C + D

n = int(input())

word = []
for i in range(n):
    word.append(input())

word_data = [0]*26  # 알파벳은 26글자 , 단어는 최대 8글자 이므로 10의 8승을 데이터가 할당되지않은값으로 둔다.

for i in range(n):
    k = 0
    size = len(word[i])  # 단어의 길이만큼
    for j in range(size-1, -1, -1):
        if k > size-1:
            break
        word_data[ord(word[i][k])-65] += 10**j  # 워드 데이터에 값 할당
        k += 1

# print(mword)
max_sum = 0
word_data.sort(reverse=True)  # 내림차순 정렬
size = 9
for i in range(26):
    if word_data[i] != 0:  # 사용중인 알파벳인경우에 한에
        word_data[i] *= size
        size -= 1
        max_sum += word_data[i]

print(max_sum)
