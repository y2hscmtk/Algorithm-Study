# https://www.acmicpc.net/problem/7490
'''
1부터 N까지의 수를 오름차순으로 쓴 수열 1 2 3 ... N을 생각하자.
그리고 '+'나 '-', 또는 ' '(공백)을 숫자 사이에 삽입하자(+는 더하기, -는 빼기, 공백은 숫자를 이어 붙이는 것을 뜻한다). 
이렇게 만든 수식의 값을 계산하고 그 결과가 0이 될 수 있는지를 살피자.

각 테스트 케이스의 결과는 한 줄을 띄워 구분한다.
1+2-3

1+2-3+4-5-6+7
1+2-3-4+5+6-7
1-2 3+4+5+6+7
1-2 3-4 5+6 7
1-2+3+4-5+6-7
1-2-3-4-5+6+7
'''
'''
아이디어 : 재귀함수를 이용하여 길이가 2n-1이 된 경우, 수식의 결과가 0인지 확인하여 0이라면 출력한다.
+,-, 이어붙인 수를 + 하기, 이어붙인 수를 -하기
=> eval()활용하기
'''

# 가장 오른쪽 숫자, 수식
def calc(num,result):
    # 재귀함수 종료 조건 설정
    if num == n+1: 
        # 수식의 결과가 0인지 확인한다
        tmp = result.replace(" ","") # 공백제거
        if eval(tmp) == 0:
            print(result) # 식을 출력한다.
        return  # 재귀함수 탈출
    
    # 아직 식이 완성되지 않았다면
    # 공백 연산
    # 현재 1+2가 있다고 가정 1+2 3이 됨
    calc(num+1,result+' '+str(num))
    # 더하기 연산
    calc(num+1,result+"+"+str(num))
    # 빼기 연산
    calc(num+1,result+"-"+str(num))


for _ in range(int(input())): # 첫째줄에는 테스트케이스의 수가 주어진다.
    n = int(input()) # 1,2,3..n까지의 수열을 이용한다.
    calc(2,"1") # 현재 수식은 1이므로, 다음에 넘겨야 할 숫자는 2
    print("") # 각 테스트 케이스의 결과는 한 줄을 띄워 구분한다.
