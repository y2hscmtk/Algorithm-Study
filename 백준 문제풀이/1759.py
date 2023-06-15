# https://www.acmicpc.net/problem/1759
'''
아이디어1
입력받은 알파벳 배열에서 L개의 알파벳을 뽑는다.
뽑힌 알파벳을 정렬해서 출력한다.
순열과 조합을 적절히 이용하면 될듯?
'''
from itertools import combinations

L,C  = map(int,input().split()) # C개의 문자열 중에서 L개를 사용할것임(중복 허용x)

data = list(input().split()) # 알파벳 세트 입력받기

result = [] # 정답을 저장할 배열
# combination을 이용하므로, 중복되는 경우가 없음
for array in combinations(data,L):
    # 추출한 배열 정렬
    select = list(array)
    
    # 암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 
    # 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다.
    # 위 조건을 만족하는지 확인해야함
    m,z = 0,0 # 모음, 자음의 개수
    for alphabet in select:
        if alphabet in "aeiou":
            m+=1 # 모음 개수 증가
        else:
            z+=1
    
    # 조건을 만족한다면 삽입 진행
    if m>=1 and z>=2:
        select.sort() # 정렬
        result.append(select) # 정답 배열에 삽입

# result배열 정렬 필요
result.sort()

for array in result:
    # 공백을 두고 출력하면 안됨
    for alpahbet in array:
        print(alpahbet,end='')
    print('')