#Task1: Calculate Factorial Using a Function

def factorial(n):                                  #function named factorial
    if n<2:
        return 1
    else:
        return n*(factorial(n-1))

num=int(input("Enter a number: "))
result=factorial(num)
print("Factorial of", num, "is: ", result)

