# https://www.acmicpc.net/problem/1181

# 백준 1181번

'''
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
'''

n = int(input())

data = []

for _ in range(n):
    data.append(input())

# 중복값 제거
data = list(set(data))  # set은 중복과 순서를 허용하지않음

data.sort()  # 사전순으로 정렬하고, 길이순으로 재정렬
data.sort(key=lambda x: len(x))  # key=lambda x 구문 뒤에 붙은 조건에 맞춰 정렬


for i in data:
    print(i)
