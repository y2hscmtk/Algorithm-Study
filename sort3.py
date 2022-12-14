# 두 배열의 원소 교체

# 동빈이는 두 개의 배열 A와 B를 가지고 있다. 두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수이다.
# 동빈이는 최대 K번의 바꿔치기 연산을 수행할 수 있는데, 바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 
# 두 원소를 서로 바꾸는 것을 말한다. 동빈이의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이며, 여러분은 동빈이를 도와야 한다.

# N, K 그리고 배열 A와 B의 정보가 주어졌을 때, 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하시오.
# 예를 들어 N = 5, K = 3이고 배열 A와 B가 다음과 같다고 하자.

# 배열 A = [1,2,5,4,3]
# 배열 B = [5,5,6,6,5]

# 이 경우, 다음과 같이 세 벙의 연산을 수행할 수 있다.

# 연산 1) 배열 A의 원소 1과 배열 B의 원소 6을 바꾸기
# 연산 2) 배열 A의 원소 2와 배열 B의 원소 6을 바꾸기
# 연산 3) 배열 A의 원소 3과 배열 B의 원소 5를 바꾸기

# 세번의 연산 이후  배열 A와 배열 B의 상태는 다음과 같이 구성된다.

# 배열 A = [6,6,5,4,5]
# 배열 B = [3,5,1,2,5]

# 이때 배열 A의 모든 원소의 합은 26이 되며, 이보다 더 합을 크게 만들 수는 없다. 따라서 이 예시의 정답은 26이 된다.

# 입력조건 : 첫번째 줄에 N K가 공백으로 구분되어 입력된다. 두번째 줄에 배열 A의 원소들이 공백으로 구분되어 입력되고 세번째 줄에 배열 B의 원소들이 공백으로 구분되어 입력된다.

# 출력조건 : 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최대값을 출력한다.


# 아이디어 : 배열 A를 크기순으로 len(A)-k번째 수까지를 더하고 남은 K개의 수와 배열 B에서 가장 큰 K개의 수를 비교하여 B의 수가 더 크다면 그만큼 바꿔치기 연산을 수행한다.

# # n,k 공백으로 구분하여 정수로 입력받기
# n, k = map(int,input().split())

# #공백으로 구분하여 정수를 입력받아 리스트 A에 저장
# a = list(map(int,input().split()))

# #공백으로 구분하여 정수를 입력받아 리스트 B에 저장
# b = list(map(int,input().split()))

# result = 0 # 합계를 더하여 출력할 변수
# #a와 b 오름차순으로 정리
# a.sort()
# b.sort()
# tmp = []
# #a에서 큰 데이터 저장
# for i in range(1,len(a)-k+1):
#     result += a[-i]

# # #b에서 k개의 큰 데이터 따로 저장
# for i in range(1,k+1):
#     tmp.append(b[-i])
    
# for i in range(k):
#     if a[i]<tmp[i]:
#         result+=tmp[i]
#     else:
#         result+=a[i]
    
# print(result)

n, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort() #오름차순 정렬
b.sort(reverse=True) #내림차순 정렬 

for i in range(k):
    if a[i]<b[i]:
        a[i],b[i] = b[i],a[i] #스왑
    else:
        break #A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출

print(sum(a))