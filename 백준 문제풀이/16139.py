import sys
input = sys.stdin.readline

data = list(input())
t = int(input())

# 모든 알파벳에 대해서,
# 각 구간별로 알파벳이 몇 개 있는지 파악해서 기록해둔다
# 단 해당 인덱스의 문자도 포함하므로 초기값에 0을 넣어 배열을 생성해야함
# 예를들어 abcabb 의 경우
# dict['a'] = [0,1,1,1,2,2,2]
# dict['b'] = [0,0,1,1,1,2,2]
# dict['c'] = [0,0,0,1,1,1,1]
# 처럼 되도록 만들고,
# 알파벳 a에 대해서 구간 s,e를 입력받았다면
# => dict['a'][e+1] - dict['a'][s]를 통해 해당 구간안의 a의 개수를 알수있을것
# 예를 들어 구간이 0,3 에 문자가 a라면
# => dict['a'][4] - dict['a'][0] = 2 - 0 = 2

alphabet_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                  'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                  't', 'u', 'v', 'w', 'x', 'y', 'z']
dict = {}

for alphabet in alphabet_array:
    dict[alphabet] = [0]  # 딕셔너리 생성
    count = 0
    # 기존 문자열에 해당 알파벳이 몇개 있는지 카운팅
    for i in range(len(data)):
        if data[i] == alphabet:
            count += 1
        dict[alphabet].append(count)


for _ in range(t):
    # 미리 명령을 입력 받아두고
    w, l, r = input().split()
    l, r = int(l), int(r)
    print(dict[w][r+1] - dict[w][l])
