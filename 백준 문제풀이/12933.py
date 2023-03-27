# https://www.acmicpc.net/problem/12933
'''
오리의 울음 소리는 "quack"이다. 올바른 오리의 울음 소리는 울음 소리를 한 번 또는 그 이상 연속해서 내는 것이다. 

예를 들어, "quack", "quackquackquackquack", "quackquack"는 올바른 오리의 울음 소리이다.

녹음한 소리는 문자열로 나타낼 수 있는데, 한 문자는 한 오리가 낸 소리이다. 

오리의 울음 소리는 연속될 필요는 없지만, 순서는 "quack"이어야 한다. "quqacukqauackck"과 같은 경우는 두 오리가 울었다고 볼 수 있다.

영선이가 녹음한 소리가 주어졌을 때, 영선이 방에 있을 수 있는 오리의 최소 개수를 구하는 프로그램을 작성하시오.

영선이 방에 있을 수 있는 오리의 최소 수를 구하는 프로그램을 작성하시오. 녹음한 소리가 올바르지 않은 경우에는 -1을 출력한다.
'''

import sys
sound = list(input())

result = ["q", "u", "a", "c", "k"]

count = 0  # 오리의 수 카운트
# 배열을 돌면서, 울음소리에 해당하는게 있다면 방문처리(x로 변경)
# 더이상 방문할게 없을때까지 반복
while True:

    temp = []
    index = []
    j = 0
    for i in range(len(sound)):
        # 일치하는 음성 하나씩 체크
        if sound[i] == result[j]:
            temp.append(i)
            j += 1
        # 울음소리 하나 저장 quack
        if j == 5:
            index.append(temp[:])
            temp.clear()  # 임시 배열 초기화
            j = 0

    # 울음소리가 녹음 되었다면 방문처리
    if len(index) >= 1:
        count += 1  # 오리의 수 더하기
        for array in index:
            for i in array:
                sound[i] = 'x'  # 방문처리 => 중복 검사 방지
    else:
        # x가 아닌 문자가 남아있는지 확인
        for i in range(len(sound)):
            if sound[i] != 'x':
                print(-1)
                sys.exit(0)

        # 울음소리가 저장되지 않았다면 더 이상 확인할 필요가 없음을 의미
        # 0마리가 있는게 아니라면 마리수를 출력, 0마리라면 -1 출력
        print(-1 if count == 0 else count)
        break
