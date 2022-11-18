# https://www.acmicpc.net/problem/10817

'''
세 수가 주어졌을때 두번째로 큰 정수를 출력하라
'''

'''
세 수를 입력받은 후, 선택정렬을 거치고 가운데 인덱스를 출력
'''

# 선택 정렬 구현

data = list(map(int, input().split()))

for i in range(len(data)):
    large = i  # 0번째 인덱스부터 차례로 비교
    for j in range(i+1, len(data), 1):  # 1번째 수부터 마지막 수중 가장 큰값을 맨 왼쪽으로 이동
        if data[j] > data[large]:  # 기존 최대값보다 큰 값이 있다면
            large = j  # 해당 인덱스 저장
    data[i], data[large] = data[large], data[i]  # 가장 왼쪽으로 해당 값 옮기기

print(data[1])  # 가운데 값
