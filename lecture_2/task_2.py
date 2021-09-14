number = int(input("Enter the number of rows - "))
for a in range(number, 0, -1):
    for b in range(1, a + 1):
        print(b, end=" ")
    print("\r")

