# 가장 많이 사용된 단어 출력
# 그러한 단어가 많은 경우 ? 출력

data = input()

dict = {
    "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0,
    "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0,
    "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
}

# 모두 소문자로 변환
data = data.lower()

# 단어 수 증가
for w in data:
    dict[w] += 1

max_count = -1 # 가장 많이 등장하는 경우
# 최고 등장 횟수 찾기
for key in dict:
    temp = max_count
    max_count = max(max_count,dict[key])
    if temp!=max_count: #업데이트 되었다면
        result = key

# 해당 횟수를 갖는 단어가 2개 이상인지 확인
count = 0
for key in dict:
    if dict[key] == max_count:
        count+=1
        
if count >= 2: # 여러개 존재할경우
    print("?")
else:
    # 정답은 대문자로 출력
    print(result.upper())