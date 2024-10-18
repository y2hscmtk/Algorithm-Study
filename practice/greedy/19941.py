# https://www.acmicpc.net/problem/19941
'''
풀이 참조 여부 o

햄버거 자원은 한정되어 있으며, 영역 또한 한정되어있음
따라서 가장 가까이 있는 햄버거를 선택하는 것이
뒤의 사람들에게 있어 범위가 K인 영역내에서 햄버거를 먹을 가능성을 높여줌
'''
N, K = map(int,input().split())
table = input()

eaten = [False]*N # 해당 위치의 햄버거가 먹혔는지 여부
max_count = 0 # 섭취 가능한 최대 햄버거 수
for i in range(N):
    if table[i] == 'P': # 사람 발견시
        for j in range(i-K,i+K+1): # K영역 내에서
            if j<0 or j>=N: # 테이블 영역을 벗어나지 않는 한에서
                continue
            # 아직 먹히지 않은 햄버거 발견시 햄버거 섭취
            if table[j] == 'H' and not eaten[j]:
                eaten[j] = True # 햄버거 섭취
                max_count += 1 # 햄버거 섭취량 + 1
                break # 햄버거 섭취 완료 후 다음 사람으로 넘어가기

print(max_count)
