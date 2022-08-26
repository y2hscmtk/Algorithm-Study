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

for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1]))) # 첫번째 데이터는 문자열으로, 두번째 데이터는 정수형으로 저장
    
# 리스트안에 튜플로서 자료를 보관한 형태?

# # 낮은 성적순으로 자료 정리하기? => 오름차순으로 자료 정리 => 튜플은 정렬,스왑,등이 되지않는 자료구조임을 유의
# for i in range(n):
#     min_index = i
#     for j in range(i+1,n): #i+1번째 인덱스부터 n-1번째 인덱스까지 반복하여 최소값이 있는 인덱스 번호를 파악
#         if array[min_index][1]>array[j][1]: #더 낮은 성적이 존재한다면
#             min_index = j #j번째 인덱스를 가장 낮은 인덱스로 설정 => 반복
#     array[i][1],array[min_index][1] = array[min_index][1],array[i][1] # 스왑을 통하여 가장 낮은 성적이 가장 처음에 오도록 변경


# # 정렬이후
# for i in range(n):
#     print(array[i][0], end=' ')

# 이름을 저장할 새로운 리스트 생성
name_array = []
# 입력받은 튜플리스트에서 이름만 따로 빼어 저장
for i in range(n):
    name_array.append(array[i][0])
    
# 선택정렬 => 새로운 리스트를 만들어서 성적순에 따라 새로운 리스트의 이름 조작
for i in range(n):
    min_index = i #첫번째 인덱스가 가장 낮은 성적을 가진 인덱스라 가정
    for j in range(i+1,n): #i+1번째 수중에서 i번째 인덱스보다 낮은 값을 가진 인덱스 탐색
        if array[min_index][1]>array[j][1]: #j번째 인덱스가 더 낮은 성적을 가진 인덱스라면?
            min_data = j
    name_array[i],name_array[min_data] = name_array[min_data],name_array[i]

# 정렬 이후 낮은 성적순으로 정렬된 이름 리스트 출력
for i in name_array:
    print(i)