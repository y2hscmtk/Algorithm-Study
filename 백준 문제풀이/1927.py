# 백준 1927번 최소 힙 구현

n = int(input())  # 연산의 횟수

# 0을 입력하면 가장 작은 값을 pop하고, 그 이외의 자연수라면 최소 힙에 push한다. 최소 힙에 아무값이 없을때 pop명령이 수행된다면 0을 출력한다.

# 최소 힙 => 배열로 표현가능

min_heap = [0]*n  # 입력받은 크기만큼 배열을 생성한다.
heap_size = 0  # 힙 사이즈

j = 1  # 루트 노드의 인덱스
left_child = 2*j  # 왼쪽 자식
right_child = 2*j+1  # 오른쪽 자식
min_child = 2*j
# 팝 연산은 가장 작은 값을 배열에서 출력하고, 그 값을 배열에서 제거한다 => 나머지 노드들에 대하여 위치 재설정이 필요하다.


for i in range(n):
    item = int(input())  # 우선 사용자로부터 데이터를 입력받고
    if item == 0:
        # 팝 연산을 시행한다
        if heap_size == 0:
            print(0)
        else:
            data = min_heap[1]  # 루트 노드에 가장 작은 값이 할당되어 있기때문에, 해당 값을 반환한다.
            # 말단 노드의 값을 루트자리로 옮긴후, 자식과 비교하며 스와핑 실시
            min_heap[1] = min_heap[heap_size]
            min_heap[heap_size] = 0  # 해당 자리를 비움
            heap_size -= 1
            while True:  # 데이터의 끝까지 비교
                # 두 자식 중 더 작은 자식 탐색
                if min_heap[left_child] != 0 and min_heap[right_child] != 0:
                    if min_heap[left_child] < min_heap[right_child]:
                        min_child = left_child
                    else:
                        min_child = right_child
                if min_heap[left_child] == 0 and min_heap[right_child] == 0:
                    break
                if min_heap[j] > min_heap[min_child]:  # 부모가 자식보다 큰 상황이라면
                    # 스와핑
                    min_heap[j], min_heap[min_child] = min_heap[min_child], min_heap[j]
                    j = min_child
                else:
                    break
            print(data)
    elif item >= 1:  # 양의 정수가 입력된경우
        # 푸쉬 연산을 시행한다
        heap_size += 1  # 힙의 크기를 1 증가시키고,
        # 우선 힙의 말단에 데이터를 삽입하고, 루트노드까지 반복하며 크기를 비교한다.
        min_heap[heap_size] = item
        k = heap_size  # 현재 노드의 인덱스 번호를 저장
        while k > 1:
            root = k//2  # 부모노드 설정
            if min_heap[k] < min_heap[root]:  # 부모보다 더 작은 경우 위치를 서로 바꿔야함
                min_heap[k], min_heap[root] = min_heap[root], min_heap[k]  # 스와핑
                k = k//2  # 노드 인덱스 재설정
            else:
                break
