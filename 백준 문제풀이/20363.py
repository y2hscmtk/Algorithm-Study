# https://www.acmicpc.net/problem/20363
'''
# 아이이더3
# 첫번째 기회가 가장 중요할듯
# 첫번째(모두가 0일때)에 많이 주자(빼도 괜찮은 양만큼) 
# => 그럼 나중에 냉기를 주면서 온기가 줄어들어도 괜찮다.
목표 : 123456 12345
0 0

123456+1234 0 => +124690

124690-1234 12345 => +12345

123456 12345 완성!

정답 : 124690 + 12345 = 137035 == 정답 일치
'''
d = sorted(map(int, input().split()))
print(d[-1] + d[0]//10 + d[0])
