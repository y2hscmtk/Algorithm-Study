# https://www.acmicpc.net/problem/11721
'''
data[i:i+1]에서 i+10이 인덱스를 벗어나게 되더라도, 결과값은 가장 마지막 수까지만 출력된다.
'''

data = input()

for i in range(0,len(data),10): # 10개씩 끊어서
    print(data[i:i+10])
