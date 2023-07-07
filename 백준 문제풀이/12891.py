# https://www.acmicpc.net/problem/12891
'''
길이가 S인 문자열에서, 조건을 만족하는 길이가 P인 부분문자열의 개수 파악
<Idea>
Sliding Window
길이가 P인 Window를 설정(lf,rf로 영역 설정)
한칸 씩 윈도우를 이동하면서 조건을 만족하는지 파악, rf가 S-1이 되면 종료

'''
s,p = map(int,input().split())
array = input() 
check = list(map(int,input().split()))
change = {'A':0,"C":1,'G':2,"T":3}
# 몇개인지 미리 세어놓기 위해 dict생성
dict = {'A':0,"C":0,'G':0,"T":0}
lf,rf = 0,p-1
# 윈도우 설정
window = array[lf:rf+1]
# 윈도우 안의 dna 미리 세어 두기(전처리)
for dna in window:
    dict[dna] += 1

count = 0
while True:
    # 윈도우 구간 내의 dna수가 check과 같은지 확인
    error = False
    for dna in dict:
        # 특정 개수 이상인지 확인 => 이상이 아니다 = 에러
        if dict[dna] < check[change[dna]]:
            error = True    
            break
    # 에러가 나지 않았다면 부분문자열로 채택
    if not error:
        count+=1
    # 슬라이드 이동
    # 개수 새로 세주기
    dict[array[lf]] -= 1
    lf+=1
    rf+=1
    if rf==s:
        break
    dict[array[rf]] += 1
        
print(count)
