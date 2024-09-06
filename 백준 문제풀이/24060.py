# https://www.acmicpc.net/problem/24060
'''
병합 정렬 구현
배열 A에 K번째 저장되는 수를 출력한다. 저장횟수가 K보다 적다면 -1을 출력한다.
'''
N,K = map(int,input().split())
A = list(map(int,input().split()))
count,result = 0,0 # 저장되는 순번, 정답
# A[p..r]을 오름차순 정렬한다.
def merge_sort(p,r):
    if p < r:
        q = (p+r)//2 # mid
        merge_sort(p, q);      # 전반부 정렬
        merge_sort(q + 1, r);  # 후반부 정렬
        merge(p, q, r);        # 병합

# 병합 과정
def merge(p, q, r):
    global A,count,result
    i,j,t = p,q+1,1
    tmp = [0]*(N+1)
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i] # tmp[t] <- A[i]; t++; i++;
            t+=1; i+=1
        else:
            tmp[t] = A[j] # tmp[t] <- A[j]; t++; j++;
            t+=1; j+=1
    # 왼쪽 배열 배분이 남은 경우
    while i <= q:
        tmp[t] = A[i]
        t+=1; i+=1
    # 오른쪽 배열 부분이 남은 경우
    while j <= r:
        tmp[t] = A[j]
        t+=1; j+=1
    i,t = p,1
    # 최종 결과물을 원본 배열(A[p..r])에 저장
    while i <= r:  # 결과를  저장
        count += 1
        A[i] = tmp[t]
        if count == K:
            result = A[i]
        i+=1; t+=1

merge_sort(0,N-1)

# K번째 저장된 수를 출력한다.
# 저장 횟수가 K 보다 작으면 -1을 출력한다.
print(-1) if count < K else print(result)
