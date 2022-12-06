# https://www.acmicpc.net/problem/11652
n = int(input())

dic = {}  # 딕셔너리

'''
아이디어 : 딕셔너리를 이용하여
키로 숫자를, 값으로 해당 수의 개수를 배열의 형태로 삽입한다.
'''

for _ in range(n):
    k = int(input())
    # 이전에 저장된적 있다면, 값을 가져와서 1을 추가한후 저장
    if k in dic:
        value = dic[k]  # 값을 가져와서
        value += 1  # 수를 추가한 후
        dic[k] = value  # 누적해줌
    # 이전에 저장된적 없다면 1개라고 저장
    else:
        dic[k] = 1  # 1개 추가했다는 의미

# 만약 가장 많이 갖고 있는 정수가 여러가지라면 가장 작은 것을 출력한다
# 위의 조건에 따라 먼저 key값으로 정렬한뒤, value값으로 다시 정렬하면 된다.

# '키'값을 기준으로 정렬
dic = dict(sorted(dic.items()))
# # value값을 기준으로 정렬
# final = dict(sorted(dic.items(), key=lambda x: x[1]))

maxCount = 0  # 가장 많이 등장한 횟수
result = 0
last = 2**64
for num, count in dic.items():  # dict에서 숫자와 횟수를 가져옴
    if count >= maxCount:
        maxCount = count  # 더 많이 등장한 횟수가 있다면 해당 횟수를 맥스카운트로 설정
        if num < last:  # 횟수가 같은 경우, 더 작은 숫자를 설정
            result = num  # 해당 숫자를 정답의 숫자로 설정
            last = num  # 이전 숫자로 저장

print(result)
