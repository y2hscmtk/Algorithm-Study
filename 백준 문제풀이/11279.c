#include <stdio.h>
#include <stdlib.h>
#define MAX_ELEMENT 1000001

typedef struct
{
    int key;
} element;

typedef struct
{
    element heap[MAX_ELEMENT];
    int heap_size;
} HeapType;

HeapType *create()
{
    return (HeapType *)malloc(sizeof(HeapType));
}

void init_heap(HeapType *h)
{
    h->heap_size = 0;
}

void insert_min_heap(HeapType *h, element item)
{
    int i;
    i = ++(h->heap_size); //새로운 요소의 삽입이므로 heap_size를 증가시킨다.
    //새로운 요소가 삽입되면, 우선 제일 말단에 데이터를 삽입하고, 트리를 거슬러 올라가며 부모노드와 비교한다.
    while ((i != 1) && item.key > h->heap[i / 2].key)
    { //새로 입력받은 요소의 키값과 말단노드의 부모노드의 키값을 비교
        //새로운 요소를 삽입할 위치를 설정하는 과정
        h->heap[i] = h->heap[i / 2]; //조건에 걸리지 않았기때문에, 새로 입력받은 요소가 더 작은 상황임을 의미
        //말단의 자리로 부모를 끌어내림
        i /= 2; // 부모를 자식으로 삼고, 다시 반복 실행
    }
    h->heap[i] = item; //반복이 종료된 자리에, 새로운 노드 삽입
}

//삭제 연산 => 우선 루트의 값을 뽑아서 반환하고, 말단 노드를 루트의 자리로 옮겨 자식과 비교하며 위치 재설정
element delete_max_heap(HeapType *h)
{
    int parent, child;
    element item, temp;

    item = h->heap[1];                //루트 => 반환용
    temp = h->heap[(h->heap_size)--]; //마지막 노드의 요소
    parent = 1;                       //루트부터 비교 시작
    child = 2;                        //왼쪽 자식노드
    //루트를 제거하고 남은 노드들끼리 위치 재설정
    while (child <= h->heap_size)
    { //마지막 노드까지 비교하는것이 목표
        //루트의 자식중 더 작은 값 찾기
        if ((child < h->heap_size) && (h->heap[child].key < h->heap[child + 1].key))
            child++; //오른쪽 자식이 더 작을경우 오른쪽 자식을 비교의 대상으로 설정
        if (temp.key >= h->heap[child].key)
            break;
        h->heap[parent] = h->heap[child];
        parent = child;
        child *= 2; //왼쪽 자식을 임시로 설정
    }
    h->heap[parent] = temp;
    return item;
}

int main()
{
    int n;
    scanf("%d", &n);
    HeapType *heap;
    element e;
    heap = create();
    init_heap(heap);
    int data;

    for (int i = 0; i < n; i++)
    {

        scanf("%d", &data);
        if (data == 0)
        {
            if (heap->heap_size == 0)
                printf("0\n");
            else
            {
                e = delete_max_heap(heap);
                printf("%d\n", e.key);
            }
        }
        else
        {
            e.key = data;
            insert_min_heap(heap, e);
        }
    }
}