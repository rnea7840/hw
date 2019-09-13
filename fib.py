def fib(n): 
    if(n <= 1): 
        return n 
    else:
        return(fib(n-1) + fib(n-2)) 
n = int(input("Enter number of terms:"))
for i in range(1,n+1): 
    num=fib(i) 
print(n,"th Fibonacci number is ",num)