# https://www.acmicpc.net/problem/20437
'''
1.알파벳 소문자로 이루어진 문자열 W가 주어진다.
2.양의 정수 K가 주어진다.
3.어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이를 구한다.
4.어떤 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이를 구한다.
'''
'''
글자의 앞,뒤가 같은 경우에만 3,4조건이 둘다 충족 가능하다.
'''
from collections import defaultdict
import sys
for _ in range(int(input())):
    words = input()
    k = int(input())
    # 전체 문자열을 돌면서 각 문자가 k개 이상인 경우만 삽입
    # 딕셔너리에 <알파벳,[위치]> 형태로 삽입한다.
    dict = defaultdict(list)
    for i, word in enumerate(words):
        if words.count(word) >= k:
            # 조건을 만족하는 단어의 위치 삽입
            # aabba에서 k=2일경우 => dict['a'] = [0,1,4], dict['b'] = [2,3]
            dict[word].append(i)

    # 조건을 만족하는 문자가 없다면 -1 출력
    if not dict:
        print(-1)
        continue
    # 3번 조건, 가장 '짧은' 연속 문자열이 되기 위해선, 결국 앞과 뒤가 서로 같아야한다.
    # 딕셔너리의 조건을 만족하는 각 알파벳을 돌면서, 3번,4번의 정답을 갱신한다.
    result1, result2 = sys.maxsize, -1

    # dict['a'] = [0,1,4] 에서
    # dict['a'][0] 은 해당 인덱스까지의 부분문자열에서 a의 개수가 1개임을 의미
    # dict['a'][2] 은 해당 인덱스까지의 부분문자열에서 a의 개수가 3개임을 의미
    # 부분 문자열은 k개의 같은 문자를 가져야 함
    for i in dict:
        # k개를 포함하는 구간 파악 => 길이가 k인 윈도우
        for j in range(len(dict[i])-k+1):
            # 윈도우를 오른쪽으로 밀어가면서 길이 확인
            temp = dict[i][j+k-1] - dict[i][j] + 1

            result1 = min(result1, temp)
            result2 = max(result2, temp)
    print(result1, result2)
