test = "1-2 3-4 5+6 7"

test = test.replace(" ","") # 공백 제거
# 빼기를 기준으로 문자열 분리
test.split("-")
test.split("+")
print(test)
