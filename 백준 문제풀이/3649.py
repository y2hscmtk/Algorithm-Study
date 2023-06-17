# https://www.acmicpc.net/problem/3649
'''
몇개의 입력이 들어올지 모르니 try-except 사용해야함
첫째 줄에는 센티미터 단위로 x가 입력됨
두번째 줄에는 레고 조각의 수가 입력됨 n
이후, 나노미터 단위로 레고 조각들이 입력됨
=> 정렬 후, 이분탐색을 통해 값을 찾는다.
array의 0번째 요소를 첫번째 블록 L1으로 삼고, x-L1 한 값을 이분탐색을 통해 0번째 요소 이후 값에서 찾는다.
(단, L1의 값이 x 이상의 값인 경우, 더 이상 탐색하지 않고, danger를 출력한다.)
위와 같은 과정을 인덱스를 늘려나가면서 탐색한다.=>만족하는 값을 찾았다면 flag를 세워서 더이상 반복하지 않도록 한다.

=> 투 포인터를 이용하여 더 빠르게 개선할 수 있다.
'''
import sys
# from bisect import bisect_right
input = sys.stdin.readline


# 입력이 더이상 없을때 까지 반복
while True:
    try:
        # 구멍의 넓이가 센티미터 단위로 입력된다.
        x = int(input())
        x*= 10000000 # 나노미터 단위로 변환
        n = int(input()) # 블록의 수
        lego = []
        for _ in range(n):
            lego.append(int(input())) # 블록들이 입력된다. => 블록은 나노미터 단위이다.
        # 레고들 오름차순 정렬 => 이분 탐색을 위해
        lego.sort() 
        error = True
        # 투 포인터를 이용하여 양쪽에서 값을 하나씩 줄여나가며 값을 찾는다.
        i,j = 0,n-1
        while i<j:
            # 일치하는 두 블록을 찾으면 탈출
            if lego[i]+lego[j]==x:
                error = False
                print("yes {} {}".format(lego[i],lego[j]))
                break
            
            # 만약 양쪽값을 더한 값이 x보다 크다면
            elif lego[i] + lego[j] > x:
                j-=1 # j값을 줄인다
            else: # 더한 값이 x보다 작다면
                i+=1 # i값을 늘린다.
            
        # 블록을 막을 수 없다는 판정을 받았다면
        if error:
            print("danger")
            continue # 다음 테스트 케이스 실행
        
    except:
        break