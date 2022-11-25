# https://www.acmicpc.net/problem/1427

# 내림차순으로 정렬할것

# 파이썬의 sort 메소드를 이용 => trim sort라고 하는 합병정렬과 삽입정렬을 섞은 정렬 기법을 이용함

data = list(map(int, input()))

data.sort(reverse=True)

for i in data:
    print(i, end='')  # 공백없이 연속해서 출력하기 위함
