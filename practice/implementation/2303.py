# https://www.acmicpc.net/problem/2303
'''
N의 범위가 1000으로 적고, 각 숫자는 5개, 5개에서 3개 뽑기 5C3 = 10
1. 각 수에 대해서 숫자를 3개 뽑았을 때 일의 자리수가 가장 최대가 되는 경우의 수 찾기
2. 최대 수를 현재 N의 수와 함께 정답 배열에 삽입
3. 정답 배열을 내림 차순으로 정렬 -> N에 대해서도 정렬되는지 확인 필요
16:33 ~ 16:41
'''
import sys
input = sys.stdin.readline
N = int(input())
numbers = []
result_array = []
def find_max_num(start,count,curr):
    global temp_max_num
    # 숫자 3개 뽑은 경우 1의 자리수 확인하여 갱신
    if count == 3:
        temp_max_num = max(temp_max_num,int(str(curr)[-1]))
        return
    for i in range(start,5):
        find_max_num(i+1,count+1,curr+number_list[i])
    

for i in range(1,N+1):
    number_list = list(map(int,input().split()))
    temp_max_num = 0 # 임시 최대 수
    find_max_num(0,0,0)
    result_array.append((temp_max_num,i))

result_array.sort(reverse=True)
# 가장 큰수를 가지면서 가장 번호가 큰 사람의 번호 출력
print(result_array[0][1])