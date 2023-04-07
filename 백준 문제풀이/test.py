n, l = map(int, input().split())
p ,time = 0, 0  
for i in range(n):
    d, r, g = map(int, input().split())
    time += (d-p); p = d 
    if time % (r+g) <= r:
        time += (r-time % (r+g)) 
print(time+(l-p))