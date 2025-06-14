# Task 1: Calculate Factorial Using a Function

n=int(input("ENTER A NUMBER : "))
def facto(n):
    if(n<2):
        return 1
    else:
        return n*(facto(n-1))
result = facto(n)
print(f"THE FACTORIAL OF {n} IS: {result}")