# https://www.acmicpc.net/problem/9536
'''
다음 줄부터는 여우를 제외한 동물들의 울음소리가 <동물> goes <소리>의 형태로 입력된다. 

최소 1마리, 최대 100마리이며, 이름은 최대 100글자이고 실제로 존재하는 동물의 이름이다. 

여우를 제외한 동물의 울음소리는 한 단어이고 최대 100글자이다.

마지막 줄에는 한신이가 알고 싶어하는 질문이 주어진다. what does the fox say?
'''
t = int(input())

question = 'what does the fox say?'

for _ in range(t):
    # 전체 울음소리 입력받기
    data = list(input().split())
    while True:
        information = list(input().split())
        # 마지막 질문이라면
        if ' '.join(information) == question:
            # 정답을 출력하고
            print(*data)
            break  # 반복문 종료
        # 질문이 아니라 울음소리에 대한 정보라면
        crying = information[2]

        # 원본 배열을 돌면서 울음소리 제거
        i = 0
        while i != len(data):
            if data[i] == crying:
                data.pop(i)
                i -= 1
            i += 1
