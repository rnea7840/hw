def divisors(n):
    s = 1
    for x in range(2,n):
        if(n%x == 0):
            s += x
    return s

def main():
    for i in range(100,1000):
        if(divisors(i)==i):
            print(i)

main()
