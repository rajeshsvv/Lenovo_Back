
def fibonaci(a,n):
	a,b=0,1
	while a<n:
		print(a)
		a,b=a,a+b
		a+=1;b-=1
	print()

fibonaci(3,5)