# https://www.acmicpc.net/problem/1032
'''
문제
시작 -> 실행 -> cmd를 쳐보자. 검정 화면이 눈에 보인다. 여기서 dir이라고 치면 그 디렉토리에 있는 서브디렉토리와 파일이 모두 나온다. 

이때 원하는 파일을 찾으려면 다음과 같이 하면 된다.

dir *.exe라고 치면 확장자가 exe인 파일이 다 나온다. 

"dir 패턴"과 같이 치면 그 패턴에 맞는 파일만 검색 결과로 나온다. 

예를 들어, dir a?b.exe라고 검색하면 파일명의 첫 번째 글자가 a이고, 세 번째 글자가 b이고, 확장자가 exe인 것이 모두 나온다. 

이때 두 번째 문자는 아무거나 나와도 된다. 예를 들어, acb.exe, aab.exe, apb.exe가 나온다.

이 문제는 검색 결과가 먼저 주어졌을 때, 패턴으로 뭘 쳐야 그 결과가 나오는지를 출력하는 문제이다. 

패턴에는 알파벳과 "." 그리고 "?"만 넣을 수 있다. 가능하면 ?을 적게 써야 한다. 

그 디렉토리에는 검색 결과에 나온 파일만 있다고 가정하고, 파일 이름의 길이는 모두 같다.
'''
n = int(input())

data = []
# 출력값 입력받기
for _ in range(n):
    data.append(input())

# 첫번째 문자열을 미리 정답에 넣어두고
result = list(data[0][:])
# 그다음 문자열들을 하나씩 비교해가며 일치하지 않는단어가 존재한다면
# ?로 변환하는 작업을 실시
for i in range(n):
    for j in range(len(result)):
        # 일치하지 않는 알파벳이 존재할경우 ?로 변환
        if data[i][j] != result[j]:
            result[j] = '?'

for alphabet in result:
    print(alphabet, end='')
