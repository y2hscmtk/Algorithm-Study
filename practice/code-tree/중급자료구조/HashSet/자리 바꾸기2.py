n, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(k)]

s = [set() for _ in range(n+1)]
for i in range(1,n+1):
    s[i].add(i) # 자기 위치는 항상 도달 가능

# 현재 어디 위치에 존재하는지 확인할 수단 필요
position = [i for i in range(n+1)]

# position[i] = p -> i가 현재 p에 위치함을 의미

# a,b에 대해서 현재 어디 위치해 있는지 확인 필요
for _ in range(3):
    for a,b in edges:
        # 해당 위치에 실제 존재하는 숫자가 이동가능한 위치로 숫자 추가
        # a 위치, b 위치
        num1,num2 = position[a],position[b]
        # 이동하게 될 위치 저장
        s[num1].add(b)
        s[num2].add(a)

        # 현재 서로 위치 변경
        position[a] = num2
        position[b] = num1


for i in range(1,n+1):
    print(len(s[i]))