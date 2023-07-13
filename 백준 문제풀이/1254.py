# https://www.acmicpc.net/problem/1254
'''
현재 문자열을 뒤집은 형태를 그대로 붙였을때가, 가장 긴 팰린드롬
'''
words = list(input())


# 팰린드롬인지 확인하는 함수
def isPalindrome(words):
    for i in range(len(words)//2):
        if words[i] != words[len(words)-i-1]:
            return False
    return True


def result():
    for i in range(len(words)):
        # 현재 단어에서 부분 문자열을 뒤집어서 붙이기
        # abcb
        # 1. abcb + a = abcba (o)
        # 2. abcb + ba = abcbba (x)
        # 3. abcb + cba = abcbcba (o)
        new_words = words+words[:i][::-1]
        # 팰린드롬인지 확인
        if isPalindrome(new_words):
            return len(new_words)


print(result())
