'''
xor 결과 최대 만들기
n개의 음이 아닌 정수 중 m개의 숫자를 뽑아 모두 xor한 결과의 최대값 출력

중복 불가, 이후의 인덱스부터 수행
'''
n, m = map(int, input().split())
A = list(map(int, input().split()))

select = [0]*m

def xor_numbers():
    # select에 포함된 숫자들의 xor 결과 반환
    temp = select[0]
    for i in range(1,m):
        temp ^= select[i]
    return temp
        
result = 0
def select_number(start, idx):
    global result
    if idx == m: # m개 선택시 xor 결과 수행
        result = max(result, xor_numbers())
        return
    
    # n개의 수 중 m개 선택
    for i in range(start, n):
        select[idx] = A[i]
        select_number(i+1,idx+1)
        select[idx] = 0

select_number(0,0)
print(result)