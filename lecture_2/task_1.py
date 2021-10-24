number = int(input("Enter the number of rows - "))
for a in range(1, number + 1):
    for b in range(1, a + 1):
        print(b, end=" ")
    print("")