def rev(n):
    m=n
    r=0
    while(n>0):
        s=n%10
        r=r*10+s
        n//=10
    print("Reverse of ",m,"=",r)
    if(m==r):
        print("Palindrome")
    else:
        print("Not Palindrome")
n=int(input("Enter a No:"))
rev(n)