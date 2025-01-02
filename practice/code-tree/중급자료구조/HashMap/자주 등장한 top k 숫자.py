# 자주 등장한 top k 숫자
'''
n개의 숫자가 주어졌을 때, 자주 등장한 순으로 k개의 숫자를 출력하는 프로그램을 작성해보세요.
'''
n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = dict()
# O(n)
for num in arr:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

result_arr = []
# 빈도수 별로 배열 생성 후 정렬
# O(n + nlogn)
for num in count:
    result_arr.append([count[num],num])

result_arr.sort(reverse = True) # 빈도수 정렬

# 출력 O(n)
for i in range(k):
    print(result_arr[i][1],end=' ')
    
# 최종 시간 복잡도 : O(3n + nlogn) =~ O(nlogn)
