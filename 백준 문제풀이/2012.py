# https://www.acmicpc.net/problem/2012

'''
예상 등수
1,1,2,3,5
최대한 불만이 없게하려면
1,2,3,4,5로 배치해야함
=> 1,1,1 = 3만큼의 불만
풀이방법 
1. 정렬
2. 차를 저장
'''
array = []
n = int(input())
for _ in range(n):
    array.append(int(input())) # 예상 등수 입력받기
    
array.sort()
result = 0 # 불만
# 정렬후, 실제 등수에서 빼기
for i in range(1,n+1):
    result += abs(array[i-1]-i)
    
print(result)
