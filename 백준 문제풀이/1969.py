# https://www.acmicpc.net/problem/1969

# 유전자의 종류는 A T G C 4가지 뿐
n, m = map(int, input().split())
data = [list(input()) for _ in range(n)]

# dna dict => 같은 종류의 DNA가 여러개 있을때 사전순으로 가장 앞서는것을 출력
# => dict에서부터 사전순으로 기입
dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

dict2 = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

result = []
h = 0  # Hamming Distance

# 각 데이터의 앞 글자부터 뒷글자까지 카운팅

# 각 자리의 글자들에 대하여
for i in range(m):
    dna = [0, 0, 0, 0]
    for j in range(n):
        # 해당 dna의 개수 증가
        dna[dict[data[j][i]]] += 1
    # 가장 많이 등장하는 숫자를 정답배열에 삽입
    index = dna.index(max(dna))
    result.append(dict2[index])
    # 해당 인덱스를 제외한 DNA중에서 한개 이상 존재한다면 +1
    for k in range(4):
        if k == index:
            continue  # 가장 많은 DNA는 무시
        # 한개 이상 존재하면
        if dna[k] > 0:
            h += dna[k]

for d in result:
    print(d, end='')
print("")
print(h)
