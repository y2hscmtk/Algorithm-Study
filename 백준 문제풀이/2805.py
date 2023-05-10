# https://www.acmicpc.net/problem/2805

'''
한 줄에 연속해있는 나무의 높이가 20, 15, 10, 17이라고 하자. 상근이가 높이를 15로 지정했다면, 
나무를 자른 뒤의 높이는 15, 15, 10, 15가 될 것이고, 상근이는 길이가 5인 나무와 2인 나무를 들고 집에 갈 것이다. 
(총 7미터를 집에 들고 간다) 절단기에 설정할 수 있는 높이는 양의 정수 또는 0이다. => low : 0
어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.
=> 높이의 최대값을 구하는 것이므로, 조건을 만족하면 low = mid로 옮겨서 이분탐색 수행(mid보다 큰 값으로도 조건을 만족하는지 확인해야하므로)
'''
n,m = map(int,input().split())

tree = list(map(int,input().split()))


# 높이를 설정했을때 '적어도' m미터의 나무를 가져갈 수 있는지 확인
def satisfy(h):
    temp = 0 # 가져갈수있는 나무의 양 저장
    for i in range(n):
        if tree[i] <=h: # 설정된 높이보다 낮은 나무의 경우, 자르지 않는다.
            continue
        # 설정된 높이보다 높은 나무의 경우 잘라서 가져간다
        temp += (tree[i]-h)
    # temp를 확인했을때, 목표했던 양보다 많은 양의 나무를 가져갈 수 있다면 True
    if temp>=m:
        return True 
    else:
        return False


# 최대 높이는 1000000000
low,high = 0,1000000000
while low<high:
    mid = (low+high)//2
    # h를 mid로 설정하였을때 원하는 만큼의 나무를 가져갈수 있다면
    # 더 높은 높이로도 조건을 만족시키는지 확인해야함 => low = mid+1
    if satisfy(mid):
        low = mid + 1
        result = mid
    else: # 조건을 만족하지 못했다 => 높이를 더 줄여야한다.
        high = mid
        
print(result)