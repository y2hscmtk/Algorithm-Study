# https://www.acmicpc.net/problem/11662
'''
처음 만나는 짝수의 위치에서 lf,rf설정
결국, 시작은 항상 짝수여야함
rf를 늘려나가면서 조건 확인
'''
import sys
n, k = map(int, input().split())
s = list(map(int, input().split()))

lf, rf = -1, -1
# 최초의 짝수 위치 찾기
for i, num in enumerate(s):
    if num % 2 == 0:
        lf, rf = i, i
        break
# 짝수가 하나도 없을 수도 있기 때문
if lf == -1:
    print(0)
    sys.exit(0)

result = 0  # 가장 긴 문자열의 길이를 저장하기 위한 변수
count = 0  # 짝수인 글자의 길이
while True:
    # rf가 마지막 인덱스에 다다르면 종료
    if rf == n:
        break
    # rf가 도달한 위치가 짝수인지, 홀수인지~
    if s[rf] % 2 == 0:  # 짝수라면
        rf += 1  # rf 오른쪽으로 이동
        count += 1  # 글자 길이 증가
    else:  # 홀수라면
        # 해당 칸을 삭제 가능한지 확인
        if k > 0:  # 삭제 가능하다면
            k -= 1
            rf += 1  # 삭제 취급(글자 길이 증가x)
        else:  # 삭제할 수 없다면
            # 짝수가 나올때까지 lf 당기기
            # 그 과정에서 홀수 만나면, k+=1
            count -= 1  # 시작 위치는 항상 짝수이므로
            lf += 1
            while s[lf] % 2 != 0:
                lf += 1
                k += 1
    # 최대 길이 갱신
    result = max(result, count)
print(result)
