# 2n개 중에 n개의 숫자를 적절하게 고르기
'''
1. 총 합을 계산
2. 그룹에 들어갈 숫자 n개 선택 - 중복 불가
3. 차 업데이트
'''
n = int(input())

numbers = list(map(int,input().split()))
total = sum(numbers)
result = float('inf')
select = [0]*n
def select_num(start, idx):
    global result
    if idx == n: # n개 선택 완료시
        # 차 업데이트
        temp_sum = sum(select)
        result = min(result, abs(total - temp_sum - temp_sum))
        return
    
    for i in range(start,len(numbers)):
        select[idx] = numbers[i]
        select_num(i+1, idx+1)
        select[idx] = 0

select_num(0,0)
print(result)