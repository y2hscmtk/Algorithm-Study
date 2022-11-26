# https://www.acmicpc.net/problem/10814

'''
회원의 나이가 증가하는 순으로, 나이가 같다면 먼저 가입한 순서대로 정렬하여 출력
'''
'''
아이디어1: 데이터를 입력받을때, 반복문의 i를 가입한 순서로 적용시켜서
데이터에 함께 저장시킨후, 정렬을 하면 될듯
'''

n = int(input())

data = []

for i in range(n):  # i는 가입한 순서를 기록하기 위함이다.
    age, name = input().split()
    data.append([int(age), i, name])  # 나이, 가입순서,이름으로 배열을 생성하여 저장

# 정렬 진행
data.sort()  # 디폴트 정렬 형식으로 인해, 첫번째 요소를 기준으로 정렬후, 두번째 기준으로 정렬이 이뤄짐


# 데이터 출력
for d in data:
    print(d[0], d[2])

    
'''
리뷰 : 먼저 입력받은 데이터를 기준으로 정렬하는것을 stable sorting이라고 하는데,
파이썬의 sort는 기본적으로 stable sorting을 제공해준다고 한다.
따라서 굳이 데이터배열에 i를 삽입하여 정렬할 필요가 없었던것 같다.
'''
