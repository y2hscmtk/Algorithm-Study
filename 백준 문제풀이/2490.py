# https://www.acmicpc.net/problem/2490

'''
배(0)와 등(1)
도(배 한 개, 등 세 개), 개(배 두 개, 등 두 개), 
걸(배 세 개, 등 한 개), 윷(배 네 개), 모(등 네 개)

도는 A, 개는 B, 걸은 C, 윷은 D, 모는 E
'''
for _ in range(3):
    data = list(map(int,input().split()))
    count = data.count(1) # 등의 개수 카운팅
    if count==4: # 등이 4개면 모
        print("E")
    elif count==3: # 등이 3개면 도
        print("A")
    elif count==2: # 등이 2개면 개
        print("B")
    elif count==1: # 등이 1개면 걸
        print("C")
    elif count==0: # 등이 0개면 윷
        print("D")
