# https://www.acmicpc.net/problem/9237
'''
한 나무를 심는데 1일이 걸린다.
모든 나무가 다 자라는데 걸리는 시간은?
입력은 두 줄로 이루어져 있다. 첫째 줄에는 묘목의 수 N (1 ≤ N ≤ 100,000)이 주어진다. 

둘째 줄에는 각 나무가 다 자라는데 며칠이 걸리는지를 나타낸 ti가 주어진다. (1 ≤ ti ≤ 1,000,000)
'''
n = int(input())  # 묘목의 수

# 전체 묘목
tree_list = list(map(int, input().split()))

# 자라는데 오래걸리는 나무순으로 나무를 심어야함
# 내림 차순 정렬
tree_list.sort(reverse=True)

# 나무를 다 심은 이후시점에서 가장 오래걸리는 나무의 일수를 day에 더해주면됨
# 나무를 다 심으려면 => 일수에서 하루씩 줄여나가며 빼주면됨
for i in range(n):
    tree_list[i] -= (n-i-1)

day = n + 1  # 나무를 다 심는데 걸린 시간이 n+1(n개의 나무, 구매일 1일)

# 남은 나무들 중 가장 오래걸리는 일수를 더해줌
day += max(tree_list)
print(day)
