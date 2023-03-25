# https://www.acmicpc.net/problem/17362
'''
1,2,3,4,5
엄지,검지,중지,약지,새끼손가락

임의의 수 n을 입력했을때 그에 해당하는 답을 출력하는 프로그램 작성
'''
n = int(input())

'''
1-9-17-25
2-8-10-16 
3-7-11-15 
4-6-12-14
5-13-21-29
'''
n %= 8  # 8로 나누기

if n == 1:
    print(1)
# 0또는 2가 나옴
elif n == 2 or n == 0:
    print(2)
elif n == 7 or n == 3:
    print(3)
elif n == 6 or n == 4:
    print(4)
else:
    print(5)
