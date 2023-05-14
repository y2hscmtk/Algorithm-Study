# https://www.acmicpc.net/problem/1817

# 순서대로 상자에서 한개씩 가져온다
# 상자의 무게만큼 물건을 넣었다면 개수+1하고 다음 상자에 넣는다
import sys
n,m = map(int,input().split())
if n==0:
    print(0)
    sys.exit(0)
books = list(map(int,input().split()))

box = 1 # 필요한 상자의 개수
temp = 0 # 상자의 무게
for book in books:
    temp += book # 책의 무게만큼 temp에 더하기
    if temp<=m: # 누적 무게가 상자에 들어갈 수 있는 최대 무게보다 작다면
        continue
    # 상자에 들어갈수 있는 무게를 초과하였다면
    box += 1
    temp = book # 새롭게 무게 누적 시작
print(box)
