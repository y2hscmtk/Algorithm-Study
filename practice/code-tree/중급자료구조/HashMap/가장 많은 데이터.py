# HashMap / 가장 많은 데이터
'''
알파벳 소문자로 이루어진 문자열들이 중복을 허용하여 입력되었을때, 최대로 등장한 문자열의 등장 횟수를 출력하는 프로그램을 작성하세요.
'''
d = {}
for _ in range(int(input())):
    data = input()
    if data in d:
        d[data] += 1
    else:
        d[data] = 1

max_count = 1 # 가장 많이 등장한 횟수
for data in d:
    max_count = max(max_count,d[data])

print(max_count)
    