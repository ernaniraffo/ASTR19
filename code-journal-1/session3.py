# Write a Python program that defines a function f(x) that returns x**3 + 8. 
# In the main function of the program, call f(x) with x = 9 and print the result.  
# Use an if statement that executes if the result is larger than 27 and prints “YAY!”.


# f(x) = x^3 + 8
def f(x: int | float) -> int | float:
    return (x**3) + 8


# Main program
def main():
    res = f(9)
    print(res)
    if res > 27:
        print("YAY!")


# Run the main program if the interpreter ran this file
if __name__ == "__main__":
    main()