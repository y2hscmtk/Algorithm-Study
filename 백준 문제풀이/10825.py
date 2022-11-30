# https://www.acmicpc.net/problem/10825

'''
1.국어 점수가 감소하는 순서로
2.국어 점수가 같으면 영어 점수가 증가하는 순서로
3.국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
4.모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)

로 정렬하여 이름을 하나씩 출력하는 프로그램을 작성하라
'''

num = int(input())


# 데이터 입력받기 # 우선 모두 문자형으로 데이터를 입력받는다.
data = [list(input().split()) for _ in range(num)]

# 올바른 데이터 값을 얻기 위해서 역순으로 정렬을 시킴

# 정렬을 할때는 조건의 역순으로 거슬러 올라가며 정렬을 시키면
# 원하는 값을 얻을 수 있고, 정렬의 기준으로 자료형의 타입을 정해주는것이 꼼수이다.
# 우선 사전순으로 정렬을 시킴
data.sort(key=lambda x: x[0])
# 수학 점수가 감소하는 순서로 정렬
data.sort(key=lambda x: int(x[3]), reverse=True)  # 역순으로 정렬
# 영어 점수가 증가하는 순서로 정렬
data.sort(key=lambda x: int(x[2]))
# 국어 점수가 감소한는 순서로
data.sort(key=lambda x: int(x[1]), reverse=True)

for name in data:
    print(name[0])
