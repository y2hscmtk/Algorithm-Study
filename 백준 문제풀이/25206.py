# https://www.acmicpc.net/problem/25206
'''
구현, 문자열, 소수
20줄에 걸쳐서 치훈이의 과목명,학점,등급이 입력된다.
P/F 과목의 경우 등급이 P또는 F로 표시되는데, 등급이 P인 과목은 계산에서 제외해야 한다.
전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다.
'''
# 과목등급 점수 변환용
dict = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0,"F":0.0,"P":0.0}
count,total = 0,0 # 수강한 과목 수, 현재까지의 총 점수
for _ in range(20):
    _,score,grade = input().split()
    # P인 과목은 계산에서 제외한다.
    if grade == "P":
        continue
    score = float(score)
    grade = dict[grade]
    total += (score * grade)
    count += score

print('%.6f' % (total/count))
