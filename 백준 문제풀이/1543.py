# https://www.acmicpc.net/problem/1543
'''
단어가 중복되지 않게 몇 번 등장하는지 확인
브루트포스, 문자열
'''
words = input()
check = input()  # 이 문자가 몇번 등장하는지 알고싶음
count = 0  # 최대 몇 번 등장하는지 확인하기 위해
'''
aba/aba/ba => len = 8
aba => len = 3
<i = 0>
0~2 => count+=1 => i=3
3~5 => count+=1 => i=6

'''
for i in range(len(words)):  # 앞에서부터 확인
    temp_count = 0
    while True:
        # 종료 조건 명시
        # 끝까지 비교를 완료했다면 종료
        if i >= len(words):
            break
        # 같은 글자 존재하는지 확인
        equal = True
        # check문자열과 비교 시작
        for j in range(len(check)):
            # i가 영역을 벗어나지 않는지 확인필요
            if i == len(words):
                equal = False
                break
            if words[i] != check[j]:
                equal = False  # 같지 않음
                break
            i += 1  # 다음 문자열과 같은지 비교
        if equal:  # 일치할 경우
            temp_count += 1
        else:
            i += 1  # 다음 문자에서 비교
    # 정답 업데이트
    count = max(temp_count, count)
print(count)
