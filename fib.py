def fib(l):
	if l==0:
		return 1
	if l==1:
		return 1
	if l==2:
		return 2
	return fib(l-1)+fib(l-2)
n = int(input())
l = 0
s = 1

while s<=n:
	m = fib(l)
	print(m)
	l = l+1
	s = s+1

