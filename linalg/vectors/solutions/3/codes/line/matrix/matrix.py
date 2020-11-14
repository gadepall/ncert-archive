#To find the number od possible odrders of matrices to represent n elements
 #number of elements=n
#total possible orders = {total no of divisors}=d
def possible_orders(n):
	d=0
	for i in range(1,n+1):
		if (n%i)==0:
			d+=1
	return(d)

print("Total possible orders for 18 elements  = "+str(possible_orders(18)))
print("Total possible orders for 5 elements  = "+str(possible_orders(5)))
