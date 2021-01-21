print("Enter the first number:")
a = float(input('>'))
print("Enter the second number:")
b= float(input('>'))
print("Enter the operation to be donefrom the range of (+, -, *, /, %, remainder):")
c= input('>')

if (c=='+'):
	d = a+b
	print("The sum is:",d)
elif (c=='-'):
	d = a-b
	print("The difference is:",d)
elif (c=='*'):
	d = a*b
	print("The product is:",d)
elif (c=="/"):
	d = a/b
	print("The Quoteint is:",d)
elif (c=="remainder"):
	print("the remainder is:",d)
elif (c=="%"):
	d= a/b*100
	print("The percentage is:",d,"%")
else:
	print("the function is unknown")