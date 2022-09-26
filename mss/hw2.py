# hw2.py
from mydata import inputData, printArr, printDict  # 이것은 mydata.py를 import하는 것임
import arr2dict  # arr2dict.py를 import하는 것임

print("input a size of data:", end="")
size = int(input())

data = inputData(size)

print("--------------------------------generated data")
printArr(data)

dict = arr2dict.arr2dict(data)

print("--------------------------------result data")
printDict(dict)
