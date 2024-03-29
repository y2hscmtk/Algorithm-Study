# https://www.acmicpc.net/problem/13164
'''
인접한 사람들끼리의 키의 합을 최소로 하기 위해선
조를 나눌 '경계'를 잘 설정해야함
6명을 3개의 조로 나누는 상황을 가정할때
0/0,0,0,0/0
0,0/0,0/0,0
0,0/0,0,0/0
등으로 나눌 수 있고, 이는 경계를 2개 골라야 함을 의미한다
=> n명을 k개의 조로 나누면 k-1만큼의 경계를 골라야 한다.

사람이 여러명 있을때 가장 큰사람과 가장 작은 사람의 키 차이는
인접한 사람의 키 차이를 더한 값과 같다
1,3,5 와 같이 있을때, 1,3의 차이는 2이고 3,5의 차이는 2이므로
1,3,5 그룹에서 가장 큰 사람과 가장 작은 사람의 키 차이는 4이다.

이를 이용해서 모든 인접한 사람들의 키 차이를 구해 저장한 배열을 만들고
오름차순으로 정렬한다.
6명의 경우 인접한 키 차이 배열은 5개의 인덱스를 갖게 될 것이고
3개의 그룹으로 나눈다고 할 때, 5개의 인덱스 중 2개의 인덱스는 경계 값으로 무시 될 수 있다.

1,4,2,7,8,10 와 같이 있을때 인접한 키 차이 배열은
3,2,5,1,2 이 되고, 이 중에서 경계로 5와 3을 지정하면
1/4,2/7,8,10 으로 조가 나뉘게 되고, 각각의 키 차이는 0/2/3이 되어 합은 5가 된다.
따라서 키 차이 배열 3,2,5,1,2를 오름차순 정렬한 뒤(1,2,2,3,5)
이 중에서 가장 큰 k-1개의 값들을 무시하고 더하면 최소값이 된다.(1+2+2 = 5) 
'''
n,k = map(int,input().split())
# 키 배열
h = list(map(int,input().split()))
# 인접한 키 배열
array = []
for i in range(1,len(h)):
    array.append(h[i]-h[i-1])
    
# 인접한 키 배열 오름차순 정렬
array.sort()

# 가장 큰 k-1개 무시하고 나머지 값들 합하여 출력
# n-1 - (k-1) = n-k
print(sum(array[:n-k]))
