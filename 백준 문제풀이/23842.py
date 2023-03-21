# https://www.acmicpc.net/problem/23842
'''
성냥개비를 적절히 배치하여 식을 만족하는지 확인
동빈이가 연습할 문제는 '올바른 수식 만들기' 문제이고, 다음의 조건들을 만족해야 한다.

수식은 □□+□□=□□ 의 형태이고, 각 빈칸에는 0~9의 숫자가 들어간다.
모든 수는 항상 두 자릿수에 맞게 표현해야 한다.
예시로, 27인 경우에는 '27', 5인 경우에는 '05'로 표현한다
'+' 와 '=' 에도 각각 두 개의 성냥개비가 필요하다. 
N개의 성냥개비가 주어졌을 때, 성냥을 모두 사용하여 조건을 만족하는 수식을 만들 수 있을까? 가능한 답이 없다면 impossible을 출력한다.
'''
'''
브루트포스기법으로, 모든 경우의 수를 대입해보면 될듯
'''
import sys
dict = {"1": 2, "2": 5, "3": 5, "4": 4, "5": 5,
        "6": 6, "7": 4, "8": 7, "9": 6, "0": 6}


# 성냥개비의 수 입력받기
n = int(input())

n -= 4  # '+',"="에 필요한 성냥개비는 미리 제거하고 생각


# 성냥개비 개수 카운터
def count_matches(count, number):
    for i in range(len(number)):
        count += dict[number[i]]
    return count


# 3중 반복문을 이용하여 숫자 3개 뽑기
# 첫번째 수에 해당하는 수 정하기
for i in range(100):
    count = 0  # 성냥개비 개수 카운터
    num1 = str(i).zfill(2)
    # 성냥개비 개수 카운트
    count = count_matches(count, num1)
    # 문제에서 사용하라고 주어진 성냥개비 개수보다 더 많이 사용했다면 다음수로
    if count > n:
        continue
    # 두번째 수에 해당하는 수 정하기
    for j in range(100):
        count2 = count
        # 빈공간에 0 채우기
        num2 = str(j).zfill(2)
        # 성냥개비 개수 카운트
        count2 = count_matches(count2, num2)
        # 문제에서 사용하라고 주어진 성냥개비 개수보다 더 많이 사용했다면 다음수로
        if count2 > n:
            continue

        # 정답에 해당하는 수 정하기
        for k in range(100):
            count3 = count2
            num3 = str(k).zfill(2)
            # 성냥개비 개수 카운트
            count3 = count_matches(count3, num3)
            # 문제에서 사용하라고 주어진 성냥개비 개수보다 더 많이 사용했다면 다음수로
            # 성냥개비를 모두 사용했는지 확인
            if n == count3:
                # 모두 사용하였다면 식을 만족하는지 확인
                if int(''.join(num1)) + int(''.join(num2)) == int(''.join(num3)):
                    print(f'{num1}+{num2}={num3}')
                    sys.exit(0)

# 반복문을 수행하는동안 프로그램이 종료되지 못했다면 impossible
print("impossible")
