import programs 

def main():
    print("Choose an operation:")
    print("1. Prime Number Check")
    print("2. Factorial Calculation")
    print("3. Fibonacci Sequence")
    print("4. Sum of Digits")
    print("5. Reverse a Number")
    print("6. Check for Palindrome Number")
    print("7. Armstrong Number Check")
    print("8. Check if a Number is Perfect")
    print("10.Exit")
    while(True):

        choice = int(input("Enter the number of the operation you want to perform: "))

        if choice == 1:
            n = int(input("Enter a number: "))
            print(programs.is_prime(n))
        
        elif choice == 2:
            n = int(input("Enter a number: "))
            print(programs.factorial(n))
        
        elif choice == 3:
            n = int(input("Enter the position in the Fibonacci sequence: "))
            print(programs.fibonacci(n))
        
        elif choice == 4:
            n = int(input("Enter number: "))
            print(programs.sum_of_digits(n))
        
        elif choice == 5:
            n = int(input("Enter  number: "))
            print(programs.reverse_number(n))
        
        elif choice == 6:
            n = int(input("Enter  number: "))
            print(programs.is_palindrome(n))
        
        elif choice == 7:
            n = int(input("Enter  number: "))
            print(programs.is_armstrong(n))
        
        elif choice == 8:
            n = int(input("Enter a number: "))
            print(programs.is_perfect(n))

        elif choice==10:
            print("Exist ")
            break
        else:
            print("Invalid choice.")
           

main()
