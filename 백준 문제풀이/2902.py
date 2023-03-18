# https://www.acmicpc.net/problem/2902
'''
첫 번째는 성을 모두 쓰고, 이를 하이픈(-)으로 이어 붙인 것이다. 예를 들면, Knuth-Morris-Pratt이다. 이것을 긴 형태라고 부른다.
두 번째로 짧은 형태는 만든 사람의 성의 첫 글자만 따서 부르는 것이다. 예를 들면, KMP이다.

긴 형태의 알고리즘 이름이 주어졌을 때, 이를 짧은 형태로 바꾸어 출력하는 프로그램을 작성하시오.
'''
'''
-를 기준으로 문자열을 분리한후, 첫번째 문자들을 이어서 출력하면 될듯
'''
array = input().split('-')

short = []

for data in array:
    short.append(data[0])

for word in short:
    print(word, end='')
