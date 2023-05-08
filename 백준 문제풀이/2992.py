from itertools import permutations

x = list(input())
number = int(''.join(x))
new = set()

for array in permutations(x, len(x)):
    new.add(int(''.join(array)))
new = list(new)
new.sort()
# x랑 구성이 같은 수중, x보다 큰 수 파악
for i in range(len(new)):
    if new[i] == number:
        if i+1 < len(new):
            print(new[i+1])
        else:
            print(0)
