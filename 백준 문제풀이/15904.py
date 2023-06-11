# https://www.acmicpc.net/problem/15904
data = list(input())

check = "UCPC" # 비교대상
j = 0 # 비교대상의 인덱스
success = False
for i in range(len(data)):
    if data[i]==check[j]:
        j+=1
    # UCPC가 완성되었다면 종료
    if j==4:
        success = True
        break
print("I love UCPC") if success else print("I hate UCPC")
