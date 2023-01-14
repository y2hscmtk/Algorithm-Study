# https://www.acmicpc.net/problem/1991

'''
이진 트리를 입력받아 

전위 순회(preorder traversal), 
중위 순회(inorder traversal), 
후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.

예를 들어 위와 같은 이진 트리가 입력되면,

전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
가 된다.
'''

n = int(input())

# 트리로 사용할 딕셔너리 생성
tree = {}


# 전위순회 VLR
def preorder(root):
    # .이 아닐때만 출력
    if root != '.':
        print(root, end='')  # v
        preorder(tree[root][0])  # L
        preorder(tree[root][1])  # R


# 중위순회 LVR
def inorder(root):
    # .이 아닐때만 출력
    if root != '.':
        inorder(tree[root][0])  # L
        print(root, end='')  # v
        inorder(tree[root][1])  # R


# 후위순회 LRV
def postorder(root):
    # .이 아닐때만 출력
    if root != '.':
        postorder(tree[root][0])  # L
        postorder(tree[root][1])  # R
        print(root, end='')  # v


for _ in range(n):
    # 데이터 입력받기
    nodes = input().split()
    # 루트 : 왼쪽자식, 오른쪽자식으로 저장
    tree[nodes[0]] = [nodes[1], nodes[2]]

# 결과 출력
preorder('A')
print()
inorder('A')
print()
postorder('A')
