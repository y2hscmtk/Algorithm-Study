# https://www.acmicpc.net/problem/4659
'''
1. a,e,i,o,u 중 하나를 반드시 포함하여야 한다.
2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안된다.
3. 같은 글자가 연속적으로 두번 오면 안되나, ee와 oo는 허용한다.
'''
while True:
    p = input()
    data = [False]*len(p) # True면 모음, False면 양수
    if p == "end":
        break
    error = False # 에러 여부
    # 1. 모음이 반드시 포함되어야 한다.
    for i in range(len(p)):
        # 같은 글자가 연속으로 오면 안된다.
        if i>0 and p[i] == p[i-1] and p[i] not in ['e','o']:
            error = True
            break # 더 이상 살펴 볼 필요가 없음
        # 현재 문자가 모음 중 하나라면
        if p[i] in ['a','e','i','o','u']:
            data[i] = True
        else:
            data[i] = False
        # 모음이 3개 혹은 자음이 3개 연속으로 오면 안된다.
        if i>=2 and data[i] == data[i-1] and data[i-1] == data[i-2]:
            error = True
            break
    if data.count(True) == 0: # 모음이 한 개도 없다면
        error = True
    if not error:
        print(f'<{p}> is acceptable.')
    else:
        print(f'<{p}> is not acceptable.')