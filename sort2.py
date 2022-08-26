# 성적이 낮은 순서로 학생 출력하기

# N명의 학생 정보가 있다. 학생의 정보는 학생의 이름과 학생의 성적으로 구분된다. 
# 각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출려하는 프로그램을 작성하라

# 입력조건
# 첫 번째 줄에 학생의 수 N이 입력된다.
# 두 번째 줄부터 N+1번째 줄에는 학생의 이름을 나타내는 문자열 A와 학생의 성적을 나타내는 정수 B가 공백으로 구분되어 입력된다.
# 문자열 A의 길이와 학생의 성적은 100 이하의 자연수이다.

# 출력조건
# 모든 학생의 이름을 성적이 낮은 순서대로 출력한다. 성적이 동일한 학생들의 순서는 자유롭게 출력해도 괜찮다.

# 학생의 수 n입력받기
n = int(input())

array = []

# for i in range(n):
#     input_data = input().split()
#     array.append((input_data[0], int(input_data[1]))) # 첫번째 데이터는 문자열으로, 두번째 데이터는 정수형으로 저장
    
# # 키를 이용하여 점수를 기준으로 정렬
# array = sorted(array,key=lambda student: student[1])

# for studend in array:
#     print(studend[0],end=' ')

for i in range(n):
    input_data = input().split()
    array.append((int(input_data[1]),input_data[0])) # 성적, 이름순으로 정렬

#오름차순으로 정렬
array.sort()

for i in range(n):
    print(array[i][1],end=' ')