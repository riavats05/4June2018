print "Find the Factorial of a number"
def fact(num):
	if num==1:
		return 1
	else:
		return num*fact(num-1)
num=(int)(raw_input("Enter a number: "))
if num<0:
	print "Factorial of -ve number is not possible"
elif num==0:
	print "Factorial is 1"
else:
	print "Factorial of ", num , " is ", fact(num) 
