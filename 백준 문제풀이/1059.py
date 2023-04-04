l = int(input())  # 집합의 크기
array = list(map(int, input().split()))
# 먼저 오름차순 정렬 필요
array.sort()
n = int(input())
# 입력받은 숫자가 기존 배열에 존재한다면 0춫력
if n in array:
    print(0)
else:
    min, max = 0, 0
    for i in range(l):
        if n < array[i]:
            max = array[i]
            break
        if n > array[i]:
            min = array[i]
    # 구간 정하기
    min += 1
    max -= 1
    # 수학 공식 적용
    print((n-min)*(max-n+1) + max-n)
