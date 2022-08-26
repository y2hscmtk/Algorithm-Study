# 위에서 아래로

# 하나의 수열에는 다양한 수가 존재한다. 이러한 수는 크기에 상관없이 나열되어 있다. 이 수를 큰 수부터 작은 수의 순서로 정렬해야 한다. 
# 수열을 내림차림순으로 정렬하는 프로그램을 만드시오.

# 입력조건
# 첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다.
# 둘째 줄부터 N+1번째 줄까지 N개의 수가 입력된다. 수의 범위는 1 이상 1000000이하의 자연수이다.
# 입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분하여 출력한다. 동일한 수의 순서는 자유롭게 출력해도 괜찮다.

# 정렬 알고리즘 : 선택정렬, 삽입정렬, 퀵정렬, 계수 정렬,등 활용가능

# 선택정렬 이용

n = int(input())

# 입력받은 정수를 저장할 배열(리스트) 생성
array = []
for i in range(n): #n개의 자연수를 입력받을것이기 때문에 n번 반복
    array.append(int(input())) #정수로 입력받아 array에 append
    
# 선택정렬 실시
# array = sorted(array,reverse =True) 파이썬 기본 라이브러리로 가능

for i in range(n):
    max_index = i
    for j in range(i+1,n):
        if array[max_index]<array[j]: #내림차순은 큰 수가 가장 첫번째 인덱스에 존재해야 함 
            max_index = j
    array[i],array[max_index] = array[max_index],array[i] #두 수의 위치를 스왑
             
for i in array:
    print(i,end =' ')
    
    
