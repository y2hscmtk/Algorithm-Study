# https://www.acmicpc.net/problem/1107

'''
수빈이는 TV를 보고 있다. 수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.

리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. 

+를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, -를 누르면 -1된 채널로 이동한다.

채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.

수빈이가 지금 이동하려고 하는 채널은 N이다. 

어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오. 

수빈이가 지금 보고 있는 채널은 100번이다.
'''
'''
망가진 버튼을 제외하고는 버튼을 누를수 있다.
5457 / 6,7,8 인 경우
5455번을 누른뒤 +버튼을 2번 누르므로 4 + 2 = 6 이 정답이 된다.
'''
# 아이디어 1 => 폐기
# # 앞에서부터 측정하여 망가지지 않은 버튼이면 누른다.
# # 망가진 버튼이면 가장 가까운 숫자를 누른다. => 이 경우 큰 수/작은 수로 경우가 나눠짐
# # +, -를 적절히 사용하여 인접한 숫자를 만든다
# # 위 모든 과정을 카운팅 한 뒤, 과정이 끝나고 최소횟소를 갱신한다.

# # 원하는 숫자에 도달할때까지
# while True:
#     count = 0  # 버튼을 누른 횟수를 기록
#     data = []  # 누른 버튼을 기록
#     for number in n:
#         # 망가진 숫자가 아니라면 누른다.
#         if int(number) not in broken:
#             data.append(int(number))
#         else: # 망가진 숫자인 경우

# 아이디어 2
# 중복 순열을 이용하여 망가지지 않은 숫자들에서 n의 자리수만큼 카드를 뽑아서(1234의 경우 4장) n의 자리수만큼 카운팅을 늘리고
# 숫자가 일치하는지 확인한후, 일치하지않는다면 일치할때까지 +,-버튼을 누른다. 이후 원본숫자와 차를 구하면 해당 수가 버튼을 누른 횟수가 될것이므로
# 버튼을 누른 수와 자리수를 더한 값을 최소 횟수로 간주,기존의 최소횟수와 비교한다.
import sys
from itertools import product  # 중복 순열을 이용하기 위해
n = list(input())  # 이동하려고 하는 채널
m = int(input())  # 망가진 버튼의 갯수
buttons = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
broken = []  # 망가진 버튼이 0개일수도 있으므로, 집합을 먼저 생성한다.
if m != 0:
    broken = list(input().split())  # 망가진 버튼
broken = set(broken)  # 교집합을 제거하기 위해 집합 자료형으로 변환
# 멀쩡한 버튼들
buttons = buttons - broken

min_count = sys.maxsize  # 버튼을 누를때 필요한 최소횟수를 기록

goal = int(''.join(n))

# 수빈이는 현재 100번을 보고 있다.
# 따라서 1번 버튼이 망가져있어도 +,-버튼을 통해 이동할수 있음
# 이동하려는 채널의 길이가 100번대인지 확인하여 최소값 갱신
if len(n) == 3 and n[0] == '1':
    # 숫자 2개만 뽑아서 처리
    for data in product(buttons, repeat=2):
        # 첫번째 숫자는 고정
        number_product = [n[0]]
        number_product.append(''.join(data))
        number = ''.join(number_product)
        # +,- 버튼을 이용하여 원하는 숫자를 만드는 경우와
        # 보유하고 있는 버튼을 이용하여 원하는 숫자를 만드는 경우와
        # 보유하고 있는 버튼과 +,- 버튼을 이용하여 원하는 숫자를 만드는 경우 고려

        # 보유하고 있는 버튼을 눌러서 원하는 숫자를 바로 만든 경우 => 버튼을 2번 누른것에 해당함
        if number == ''.join(data):
            min_count = min(min_count, 2)
        else:  # 근접한 숫자에 +,-버튼을 눌러서 원하는 숫자를 만들때와 +,-버튼만을 이용할때를 고려
            min_count = min(min_count, min(
                2+abs(int(number)-goal), abs(goal-100)))
# # 이동하려는 숫자가 2자리 혹은 1자리수 번호일경우
# elif len(n) < 3:
#     # 100에서 -버튼을 눌러 이동하거나, 보유하고있는 버튼을 눌러서 이동하거나
#     for data in product(buttons,repeat=len(n)):

else:
    # n의 자리수만큼 데이터 뽑기
    for data in product(buttons, repeat=len(n)):
        count = len(n)  # 지금까지 누른 번호의 횟수
        number = ''.join(data)
        # 원하는 숫자와 같은지 비교
        if number == ''.join(n):  # 원하는 숫자를 찾았다면 최소 버튼 횟수 갱신
            min_count = min(min_count, count)
        # 원하는 숫자가 아닐경우
        else:
            # 두 숫자의 차만큼 +,-버튼이 눌릴것이므로 차를 더한값과 기존 최솟값을 비교한다.
            # 혹은 100에서 -만 눌러서 내려갈수도 있으므로 해당 경우도 고려
            min_count = min(min_count, min(
                count+abs(int(number)-goal), abs(100-goal)))
print(min_count)
