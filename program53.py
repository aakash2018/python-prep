largest = float("-inf")
smallest = float("inf")

while True:
    number = float(input("Enter a number (enter 0 to stop): "))

    if number == 0:
        break

    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

if largest != float("-inf") and smallest != float("inf"):
    print("Largest number:", largest)
    print("Smallest numberL", smallest)
else:
    print("No numbers were entered.")
