# https://www.acmicpc.net/problem/17610

# 입력받은 숫자들을 더하고 빼서 만들수 있는 모든 수를 만들면 됨
k = int(input())
weights = list(map(int, input().split()))
# 만들수 있는 배열의 최대 크기
max_size = sum(weights)

# 만들수 있는 숫자들
candidate = [0]

# 무게를 하나씩 뽑는다.
for weight in weights:
    # 기존에 만들수 있는 숫자들에 더하고 빼서 삽입
    candidate = list(candidate)
    temp = [] # 만들 수 있는 무게를 만들 임시 배열 생성
    for cw in candidate:
        temp.append(cw+weight)  # 기존에 있는 수들과 더해서 만들 수 있는 수
        temp.append(abs(cw-weight))  # 기존에 있는 수들과 빼서 만들 수 있는 수
    candidate.extend(temp)  # candidate배열에 temp배열 확장
    candidate = set(candidate)  # 중복값 제거
count = 0

# candidate에는 만들 수 있는 무게로 0이 포함되어 있으므로, 1을 빼줘야함
print(max_size-(len(candidate)-1))
