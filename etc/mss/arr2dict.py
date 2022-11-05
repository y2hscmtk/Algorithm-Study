# arr2dict.py
"""
이 함수는 배열 data를 입력받아서 이를 dict로 변경하여 리턴하는 함수이다.
data = [[0, 10], [2, 11], [1, 30], [0, 50], [1, 30]]의 배열을
dict = {0: [10, 50], 2: [11], 1: [30, 30]}의 딕셔너리로 만들어 리턴한다
"""


def arr2dict(data):
    dict = {}
    check = []
    size = 0
    # 생성할 2차원 배열의 행의 개수를 구하기 위함
    for i in range(len(data)):
        if data[i][0] not in check:  # 체크리스트에 없는 key값이면 삽입
            check.append(data[i][0])
            size += 1  # 행의 개수 추가
    tmp = []
    for i in range(size):
        tmp.append(([check[i]]))  # key값에 맞춰 데이터를 삽입하기 위함

    # 해당 키값에 리스트를 삽입하는 과정
    for i in range(len(data)):
        for j in range(size):
            if data[i][0] == check[j]:  # 체크리스트에서 일치하는 key값의 인덱스를 찾고
                tmp[j].append(data[i][1])  # 해당 인덱스에 value에 해당하는 요소를 삽입한다.
                break

    for i in range(size):
        key = tmp[i][0]
        del tmp[i][0]  # 첫번째 요소는 키 값이므로 삭제
        dict[key] = tmp[i]  # 해당 키에 리스트 삽입
    return dict


if (__name__ == '__main__'):
    # 이것은 모듈 테스트용 입니다.
    data = [[0, 10], [2, 11], [1, 30], [0, 50], [1, 30]]
    dict = arr2dict(data)
    print(dict)
