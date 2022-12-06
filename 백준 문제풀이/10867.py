<<<<<<< HEAD
# https://www.acmicpc.net/problem/10867

'''
중복 뺴고 정렬하기
'''

'''
아이디어 : set()자료형은 중복을 고려하지 않으므로 set에 넣었다가 빼면 중복된 값이 없어짐
'''

x = int(input())

n = list(map(int, input().split()))

n = list(set(n))  # 중복 값 제거하고
n.sort()  # 정렬한 후에

for data in n:
    print(data, end=' ')
=======
# https://www.acmicpc.net/problem/10867

'''
중복 뺴고 정렬하기
'''

'''
아이디어 : set()자료형은 중복을 고려하지 않으므로 set에 넣었다가 빼면 중복된 값이 없어짐
'''

x = int(input())

n = list(map(int, input().split()))

n = list(set(n))  # 중복 값 제거하고
n.sort()  # 정렬한 후에

for data in n:
    print(data, end=' ')
>>>>>>> 90fb9e369d9b1c11d481814e559e6a95284cdbf9
