def lol(n):
    if n==1:
        return n
    else:
        return n*lol(n-1)
m=int(input("Enter a value: "))
if m<0:
    print("Negetive factorial cannot be determined")
elif m==0:
    print("Factorial of zero is one")
else:
    print("The factorial of",m,"is",lol(m))