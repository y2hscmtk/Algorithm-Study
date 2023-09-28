<<<<<<< HEAD
# https://www.acmicpc.net/problem/10799
'''
아이디어 : )를 만나면 (이 스택의 탑에 위치하는지 확인하여 짝이 맞는다면 탑제거
)만났을때 탑도 )라면  (의 개수만큼 +1
(만나면 기존에 스택에 존재하는 (의 개수만큼 +1한뒤에 스택에 삽입

연달아 붙어있는 레이저와 그렇지 않는 경우를 구별해야함
'''

stack = []

data = input()
result = 0 # 나눠지는 총 막대의 수
overlap = 0 # 현재까지 겹쳐져있는 총 막대수
for d in data:
    if d=='(':
        if len(stack)!=0 and stack[-1] == ')':
            result += overlap
        overlap += 1
        stack.append(d)
    elif d == ')': # 오른쪽 괄호 만날경우 왼쪽괄호가 탑에 있는지 비교
        if len(stack)!=0 and stack[-1] == '(': # 짝을 맞출수 있는 경우
            # 이 경우에는 레이저인 경우니까 +1 없음
            overlap -= 1 # 괄호 쌍 하나를 찾은거니까 -1
            result += overlap # 바닥에 깔린 수 만큼
        else: # ')' 스택의 탑이 )인 경우
            result += overlap # 바닥에 깔린 수 만큼
            stack.append(d)
    

print(result)
=======
# https://www.acmicpc.net/problem/10799
stick = input()
position = []  # 괄호의 위치를 저장하기 위함
result = 0  # 나눠진 막대의 수

for i in range(len(stick)):
    if stick[i] == '(':
        position.append(i)
    else:
        if stick[i-1] == '(':
            position.pop()
            result += len(position)
        else:
            position.pop()
            result += 1

print(result)
>>>>>>> 3a64a5223799fa6fffdffbb43ba89cdd143aa81a
