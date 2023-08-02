# https://www.acmicpc.net/problem/2083
while True:
    name,age,weight = input().split()
    # 나이가 17세보다 많거나, 몸무게가 80kg 이상이면 성인부이다. 그 밖에는 모두 청소년부이다. 
    if name=="#":
        break
    if int(age) > 17 or int(weight)>=80:
        print(name + " Senior")
    else:
        print(name + " Junior")