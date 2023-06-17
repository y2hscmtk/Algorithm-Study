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
'''
from bisect import bisect_right

# bisect_right은 일치하는 값이 없을때, 삽입할 index의 위치를 리턴한다.
# 일치하는 값을 찾았다면, 일치하는 값들중 가장 오른쪽 index+1를 리턴한다.
# 우리는 일치하는 경우에만 원하는 기능을 수행하고 싶으므로, 새로 함수를 작성한다
def check(array,target):
    index = bisect_right(array,target)
    # 일치하는 값을 찾았을 경우에
    if index-1<len(array) and array[index-1] == target:
        return True # 이분탐색의 결과, 일치하는 값을 오른쪽에서 찾았다면
    return False # 찾지 못했다면
    

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
        error = False
        for i in range(n-1): # L1을 정하는 과정
            L1 = lego[i]
            # 정해진 L1이 x이상의 값인지 확인
            if L1 >= x:
                error = True
                print("danger") # 만들 수 없음을 의미
                break
            
            # L1이 X보다 작은 값이라면 => X-L1과 일치하는 값을 오른쪽 범위에서 찾는다.
            target = x-L1
            if check(lego[i:],target): # 성공했다면
                print("yes {} {}".format(L1,target))
                break
        # 블록을 막을 수 없다는 판정을 받았다면
        if error:
            continue # 다음 테스트 케이스 실행
        
    except:
        break