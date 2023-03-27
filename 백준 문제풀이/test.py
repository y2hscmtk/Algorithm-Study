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

    index = []
    j = 0
    delete = False
    for i in range(len(sound)):
        # 일치하는 음성 하나씩 체크
        if sound[i] == result[j]:
            index.append(i)
            j += 1
        # 울음소리 하나 저장 quack
        if j == 5:
            # 해당 울음소리 방문처리 => 중복 검사 방지
            for idx in index:
                sound[idx] = 'x'
            j = 0
            delete = True  # 음성 하나를 지웠다면 => 오리음성이 한마리 이상 제거됐음을 의미

    if delete:
        count += 1  # 오리의 수 카운트 +1
    finish = True
    # x가 아닌 문자가 남아있는지 확인
    for i in range(len(sound)):
        if sound[i] != 'x': # 아직 방문하지 않은 글자가 있다면
            if j != 0 or not delete: # 
                print(-1)
                sys.exit(0)
            finish = False # 아직 끝나지 않았다는 의미로
            break
    if finish: # 모든 단어가 다 지워졌다면(위의 반복문을 문제없이 통과했다면)
        print(count) # 오리의 수 출력
        break
