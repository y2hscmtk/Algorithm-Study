# https://www.acmicpc.net/problem/4779

def cut(array,size):
    if size==1:
        print(array,end='')
        return
    # 길이가 1이 아니라면,
    # 3등분
    s_index = size//3
    m_index = 2*size//3
    first = array[:s_index]
    middle = " "*(size//3) # 공백으로 변경
    end = array[m_index:]
    
    # 반복
    cut(first,size//3)
    cut(middle,size//3)
    cut(end,size//3)


# 입력이 끝날때까지 반복
while True:
    try:
        size = int(input())
        array = "-"*(3**size)
        cut(array,3**size)
        print('')
    except:
        break

