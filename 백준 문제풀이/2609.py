def gcd(m,n):
	if m < n:
		m, n = n, m
	if n == 0:
		return m
	if m % n == 0:
		return n
	else:
		return gcd(n, m%n)

a,b = map(int,input().split())
result1 = gcd(a,b)
result2 = int(a*b/result1)
print(result1)
print(result2)