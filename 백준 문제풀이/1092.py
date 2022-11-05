# 백준 1092번
# https://www.acmicpc.net/problem/1092

# 항구에서 배로 박스를 옮긴다
# 1분마다 각 크레인은 자신이 움직일수 있는 무게보다 작거나 같은 무게의 상자를 배로 옮긴다.
# 이때, 모든 박스를 배로 옮기는데 걸리는 시간의 최소값을 구하시오.

'''
생각 정리
먼저 박스와 크레인의 무게를 내림차순으로 정렬,
박스들 중 최대값이 크레인중 최대값 보다 크다면, -1을 출력, 단 한개라도 박스의 최대값보다 큰 크레인이 존재한다면
최소 1분의 시간을 할애하여 박스를 옮기는것이 가능함

아이디어 1
박스 들 중 큰 값부터 한개씩 자신의 무게보다 크거나 같은 값을 갖는 크레인이 존재한다면, 매칭
크레인의 개수만큼 매칭을 완료하였다면 +1분을 하고 다음 차례로 넘어감
이때 모든 박스를 크레인에 실었거나, 남은 크레인의 무게로는 실을수 없는 무게의 박스라면 +1시키고 다음 차례로 넘어간다.
'''
import sys
n = int(input())  # 크레인의 개수

crane = list(map(int, input().split()))

m = int(input())  # 박스의 개수

box = list(map(int, input().split()))

minute = 0  # 걸리는 최소 시간

crane.sort(reverse=True)  # 내림차순 정렬
box.sort(reverse=True)

if box[0] > crane[0]:
    print(-1)
    sys.exit()
j = 0
index = 0

while box:  # 박스를 모두 옮길때 까지 반복
    # check = False

    if box[j] <= crane[index]:  # 가장 큰 무게의 크레인보다 작거나 같은 무게라면
        del box[j]  # 해당요소는 배에 실었으므로 제거
        index += 1
    else:
        j += 1  # 다음 배열에 대해 비교

    if j == len(box):
        j = 0
        index = 0
        minute += 1

    if index >= n:  # 한번에 실을수 있는 모든 박스를 실었다면, 초기화
        # check = True
        minute += 1
        index = 0
        j = 0
    # 가동할수 있는 모든 크레인으로 박스를 옮긴 상태일때,

    # if (0 < len(box) < len(crane)) and box[0] <= crane[len(box)-1]:
    #     if check == False:
    #         minute += 2
    #     else:
    #         minute += 1
    #     break
    # elif len(box) == 0:  # 더 이상 실을수 있는 박스가 없다면
    #     break

# if index < n:  # 마지막 시행때
print(minute)
