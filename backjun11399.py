# 백준 11399번

n = int(input())

time_list = list(map(int, input().split()))
# 시간의 최솟값을 구하기 위해선, 중복되는 시간을 최소로 줄여야 함
# 따라서 오름차순으로 배열을 정렬시킨후, 반복문을 수행하며 시간의 최소값을 구하면 된다.
time_list.sort()  # 오름차순 배열 정렬
sum = 0

for i in range(n):
    for j in range(0, i+1):
        sum += time_list[j]
print(sum)
