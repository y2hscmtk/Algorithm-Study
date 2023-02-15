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
n = list(input())  # 이동하려고 하는 채널
m = int(input())  # 망가진 버튼의 갯수
broken = list(map(int, input().split()))  # 망가진 버튼


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
