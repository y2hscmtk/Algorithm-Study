# 다음 수 구하기
# A의 다음 수는 A와 구성이 같으면서, A보다 큰 수 중에서 가장 작은 수
# 123의 경우 => 132가 다음 수임

# <<아이디어>>
# '다음 수'가 없는 경우에 대한 최종형태는?: "각 자리의 모든 수가 다음 수보다 크거나 같은 경우"
# 321 => 3>=2>=1 이므로 BIGGEST임
# BIGGEST가 아닌 경우, '다음 수'가 존재한다는 의미
# '다음 수' 찾기 알고리즘
# 1. 먼저 BIGGEST인지 아닌지 검사
# 2. BIGGEST가 아니라면, 1의 자리 수부터 거슬러 올라가며 위의 조건이 깨지는 순간 파악
# 1234의 경우 => 4,3,2,1 에서 4에서 3으로 넘어가는 순간(1의 자리수가 10의 자리수보다 크므로 변경 가능)
# 3. 조건이 깨지는 수, 이하 조건수의 오른쪽 수들 중 조건수보다 큰 수중 가장 작은 수 탐색
# 1234의 경우 => 조건수는 3, 3의 오른쪽 수는 4밖에 없음 4는 3보다 큰 가장 작은 수임
# 4. 조건수와 가장 작은 수 위치 변경 ; 1234 -> 1243
# 5. 조건수 오른쪽 수들을 다시 오름차순으로 재정렬 => 우리가 원하는 것은 '다음 수'중에서 가장 작은 수이므로

# <아이디어 검증>
# 279134399742
# 2<7< .. => not biggest
# 2,4,7,9,9,3 ... 9>3이므로, 3이 조건이 깨지는 순간
# ...399742에서 앞의 자리는 그대로 두고, 3보다 큰 수중에서 가장 작은 수 찾기
# '4'가 3보다 크면서 가장 작은 수임 => 3과 4위치 변경
# ...499732
# 4 이하의 수 오름차순으로 재정렬
# ...423799
# 정답: 279134423799

# 모든 테스트 케이스에서 위 과정 수행
for _ in range(int(input())):
    number = list(map(int,input()))
    # BIGGEEST검사
    # 1의 자리부터 검사
    # 321 => 1<=2<=3 => BIGGEST
    isBiggest = True # biggest검사
    for i in range(len(number)-1,0,-1):
        if number[i] <= number[i-1]:
            continue
        isBiggest = False # biggest가 아닌 경우
        # 123 => 3,2,1 => 조건수는 2가 되어야 함
        index = i-1 # '조건수' 탐색
        condition_number = number[i-1]
        break # 그렇지 않은 경우 발견시
    if isBiggest:
        print("BIGGEST")
        continue # 다음 테스트 케이스로 넘어가기
    # IF NOT BIGGEST
    # index의 오른쪽 수들 중에서 조건수보다 큰 수들 중 가장 작은 수 판별
    select_index = index + 1 # 바로 오른쪽 수를 선택했다고 가정 => 어차피 한 개 이상 얻어걸릴것
    for i in range(index+1,len(number)):
        if condition_number < number[i]: # 조건수 보다 큰 경우
            # 더 작거나 같은 수 발견 시(같은 경우, 더 작은 자리에서 바꾸는 것이 이득)
            if number[i] <= number[select_index]:
                select_index = i # 위치 저장
    # 스왑
    number[index],number[select_index] = number[select_index],number[index]
    # index이후 오름차순 정렬
    new_number = number[:index+1] + sorted(number[index+1:])
    for n in new_number:
        print(n,end='')
    print()