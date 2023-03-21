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
