# https://www.acmicpc.net/problem/2800
'''
1. 모든 왼쪽괄호와 오른쪽 괄호의 쌍의 위치를 기록
2. 지울 괄호의 개수를 늘려나가면서 지울 괄호의 위치를 뽑기(조합)
3. 괄호를 지운 후 정답 배열에 삽입
4. 정답 배열을 사전순으로 정렬한 후 정답 출력
'''
from itertools import combinations
data = list(input())

# 1. 괄호쌍의 위치를 기록
position = []
stack = []
for i in range(len(data)):
    if data[i] == '(':
        stack.append(i)  # 위치 기록
    elif data[i] == ')':  # 오른쪽 괄호 만나면
        # 스택에서 팝해서 쌍으로 기록
        position.append([stack.pop(), i])

result = set()  # 중복 방지
# 기록된 위치들로 괄호 제거 수행
for i in range(1, len(position)+1):  # 몇개의 괄호를 지울것인지 결정
    # 지울 괄호의 위치 선정 => 조합 이용
    for array in combinations(position, i):  # 왼쪽 괄호,오른쪽 괄호 위치들
        copy_data = data[:]  # 원본 데이터 카피
        for x, y in list(array):
            # 괄호 지우기 처리
            copy_data[x] = ''
            copy_data[y] = ''
        result.add(''.join(copy_data))  # 중복 방지

# 정렬후 정답 출력
for array in sorted(result):
    print(array)
