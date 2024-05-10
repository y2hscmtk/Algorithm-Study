# https://www.acmicpc.net/problem/1120
'''
1. A와 B의 길이가 같을 경우
    - A와 B가 일치하는 문자의 개수를 파악한다.
2. A와 B의 길이가 다를 경우
    - A가 B보다 짧으므로 B에서 A와 가장 많이 겹치는 위치를 찾고, 
        A의 앞뒤에 B와 일치하는 문자를 붙였다 가정한다.(A의 앞뒤에는 임의 문자 삽입 가능)

A와 B의 길이가 같으면서, A와 B의 차이를 최소가 되도록 했을 때, 그 차이를 출력하시오.
'''
import sys
A, B = input().split()
result = 0
if len(A) == len(B):
    for i in range(len(A)):
        if A[i] != B[i]:
            result += 1
    print(result)
else: # 길이가 다를 경우 A의 시작점을 어디로 설정해야 가장 많이 겹치는지 찾는다.
    min_diff = sys.maxsize # 최소 차이
    for start in range(0,len(B)-len(A)+1): # A를 놓을 위치 설정
        t = 0 # A의 임시 인덱스
        count = 0 # 차이값 갱신용
        for i in range(start,start+len(A)): # A의 길이만큼
            if A[t] != B[i]:
                count += 1
            t+=1
        min_diff = min(min_diff,count)
    print(min_diff)