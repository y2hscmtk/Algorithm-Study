# https://www.acmicpc.net/problem/23253
n,m = map(int,input().split()) # 교과서의 수, 교과서 더미의 수
# m개의 꾸러미를 저장할수 있는 배열 생성
array = [[] for i in range(m)]

for i in range(m):
    _ = input()
    array[i] = list(map(int,input().split()))

# 스택을 사용할 필요없이
# 한 책 더미라도, 내림차순이 아니라면 No를 출력해야함
error = False
for i in range(m):
    # 내림차순 정렬하여 새로운 배열 생성
    sorted_books = sorted(array[i],reverse=True)
    # 비교
    for j in range(len(array[i])):
        if sorted_books[j] != array[i][j]:
            error = True
            break
    if error:
        break
    
print("Yes") if not error else print("No")
