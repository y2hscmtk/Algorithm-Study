# 중급 자료구조
# HashMap / hashmap 기본
'''
n개의 명령이 주어졌을 때, 각 명령을 수행하는 프로그램을 작성해보세요. 명령의 종류는 크게 3가지 입니다.

add k v : (k, v) 쌍을 hashmap에 추가합니다. key가 k, value가 v라는 뜻입니다. 이때 만약 동일한 k가 이미 존재한다면, v로 덮어씁니다.
remove k : key가 k인 쌍을 찾아 hashmap에서 제거합니다. 잘못된 입력은 주어지지 않습니다.
find k : key가 k인 쌍이 hashmap에 있는지를 판단합니다. 있다면 해당하는 value를 출력하고, 없다면 None을 출력합니다.
'''
d = {}
for _ in range(int(input())):
    data = input().split()
    command = data[0]
    if command == "add":
        k,v = data[1],data[2]
        d[k] = v # 값 추가
    elif command == "remove":
        k = data[1]
        d.pop(k)
    elif command == "find":  
        k = data[1]
        if k in d:
            print(d[k])
        else:
            print("None")