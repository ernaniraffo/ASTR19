num = None

while type(num) != int:
    try:
        num = int(input("Enter an integer: "))
    except ValueError:
        print("Not an integer!")
        continue

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
