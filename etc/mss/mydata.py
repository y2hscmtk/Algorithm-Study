# mydata.py
import random
"""
이 함수는 [정수, 실수]인 데이터 쌍을 size개 만들어
#배열에 저장한후 이 배열을 리턴하는 함수임
"""


def inputData(size):
    data = []
    for i in range(size):
        data.append([int(random.random()*5), random.random()*size])
    return data


"""
이 함수는 배열에 들어 있는 [정수, 실수]쌍의 데이타를 출력하는
함수임
"""


def printArr(data):
    for i in range(len(data)):
        print("%2d %f" % (data[i][0], data[i][1]))


"""
이 함수는 딕셔너리를 출력하는 함수임
dict = {1: [10, 20, 30], 0: [10], 2: [30, 40, 10]}
일때
0: 10.0
1: 10.0 20.0 30.0
2: 30.0 40.0 10.0
으로 출력함
"""


def printDict(dict):
    j = 0
    for key in dict:
        print("%d: " % (key), end='')
        # value값을 []없이 출력하기 위하여
        for i in range(len(list(dict[key]))):
            print("%f" % list(dict.values())[j][i], end=' ')
        print("")
        j += 1


# 여기를 프로그램하시오
if (__name__ == '__main__'):
    dict = {1: [10, 20, 30], 0: [10], 2: [30, 40, 10]}
    printDict(dict)
