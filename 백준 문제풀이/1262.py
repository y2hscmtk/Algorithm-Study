# https://www.acmicpc.net/problem/1262
'''
N = 1 ; a
N = 2 ; b a
=> N번째 알파벳부터 첫번째 알파벳까지 반복
만들어질 타일 1개는 한 변의 길이가 2N-1인 정사각형
미리 다 그려둔 다음, 좌표에 맞는 영역
'''
import string
aList = list(string.ascii_lowercase) # abcde...

