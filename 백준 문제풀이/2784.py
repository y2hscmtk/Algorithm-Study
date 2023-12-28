# https://www.acmicpc.net/problem/2784
'''
3x3 배열이므로 별다른 로직 작성 필요없이 브루트포스로 
입력받은 문자열을 적당히 배치 한 뒤, 조건을 만족하는지 확인하면 될 것으로 보임

# 모든 경우의 수 대해서 시도해봤음에도 문제를 해결 할 수 없다면 0을 출력한다.

# 가능한 답이 여러개라면 사전순으로 가장 앞서는 것을 출력한다.
# 사전순으로 앞서는 것은 모두 한 줄로 이어붙인 9개 단어를 생각한다.
=> 입력받는 순서는 이미 사전순이므로, 앞에서부터 3개씩 뽑아서 가로로 화면에 배치한다.

예상 : 구현, 브루트포스, 문자열
'''
import sys
words = [] # 입력받은 단어들(가로,세로 상관 무관)
for _ in range(6):
    words.append(input())

selected_words = []
# 앞에서부터 3개씩 뽑는 함수
def select_word(depth): # depth는 현재까지 몇개의 수를 뽑았는지
    global selected_words
    if depth == 3: # 3개의 수를 뽑았으면 조건을 만족하는지 확인 후 종료
        check()
        return # 재귀 종료
    for i in range(len(words)):
        selected_words.append(words[i])
        select_word(depth+1)
        selected_words.pop()
    

# 모든 단어를 다 포함하는지 체크
def check():
    # print("#########")
    # print(selected_words)

    # 가로줄과 세로줄에서 만들어진 문자들을 모두 저장 후 정렬
    check_array = []
    for i in range(3):
        check_array.append(selected_words[i])
    
    for i in range(3):
        word = ''
        for j in range(3):
            word += selected_words[j][i]
        check_array.append(word)

    check_array.sort()
    # 얻은 문자열 조합과 기존에 갖고 있는 문자열이 일치한다면 모든 단어를 다 포함한 것임
    if check_array == words:
        for word in selected_words:
            print(word)
        sys.exit(0)

select_word(0)
print(0)