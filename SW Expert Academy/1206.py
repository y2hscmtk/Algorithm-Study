'''
현재 건물에서 왼쪽 건물 2채와 높이 차 비교
왼쪽 건물 2채가 현재 건물보다 낮다면, 왼쪽 조망권 확보된 가구 수 기록
오른쪽 건물 2채와 비교하여 조망권 확인
'''
for i in range(1,11): # 총 10개의 테스트 케이스 제공
    result = 0
    N = int(input()) # 건물의 개수
    tower = list(map(int,input().split()))
    for j in range(2,N-2): # 0,0, .... 0,0
        curr = tower[j]
        left_top = max(tower[j-2:j])
        right_top = max(tower[j+1:j+3])
        if curr > left_top and curr > right_top:
            result += min((curr - left_top),(curr - right_top))
    print(f'#{i} {result}')