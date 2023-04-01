# https://www.acmicpc.net/problem/11656
'''
문제
접미사 배열은 문자열 S의 모든 접미사를 사전순으로 정렬해 놓은 배열이다.

baekjoon의 접미사는 baekjoon, aekjoon, ekjoon, kjoon, joon, oon, on, n 으로 총 8가지가 있고, 

이를 사전순으로 정렬하면, aekjoon, baekjoon, ekjoon, joon, kjoon, n, on, oon이 된다.

문자열 S가 주어졌을 때, 모든 접미사를 사전순으로 정렬한 다음 출력하는 프로그램을 작성하시오.
'''
word = input()

result = [word]

for i in range(1, len(word)):
    # i번째 글자부터 끝까지 파싱해서 삽입
    result.append(word[i:])

# 사전순으로 정렬
result.sort()

# 정답 출력
for w in result:
    print(w)
