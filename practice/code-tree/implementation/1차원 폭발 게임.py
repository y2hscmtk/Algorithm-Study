BLANK = -1 # 터진 폭탄 처리
n,m = map(int,input().split())

numbers = []
for _ in range(n):
    numbers.append(int(input()))

def find_bomb():
    is_bomb = False
    for i in range(len(numbers)):
        if numbers[i] == BLANK: # 터짐처리가 되지 않은 수만 판단
            continue
        target = numbers[i]
        count = 0
        for j in range(i,len(numbers)):
            # 같은 수라면 count += 1            
            if numbers[j] != target:
                break
            count += 1 # 같은 수라면
        if count >= m: # m개 이상이라면
            is_bomb = True
            for num in range(i,i+count): # 터짐 처리
                numbers[num] = BLANK
    return is_bomb

def simulation():
    global numbers
    next_numbers = []
    # 폭탄이 터지는지 탐색
    result = find_bomb()

    # 중력 적용
    for i in range(len(numbers)):
        if numbers[i] != BLANK:
            next_numbers.append(numbers[i])
    # 원본 배열로 수정
    numbers = next_numbers

    return result
            

while True:
    result = simulation()
    if result == False: # 폭발이 발생하지 않았다면
        break

print(len(numbers))
if numbers: # 남아있는 폭탄이 존재한다면
    for num in numbers:
        print(num)