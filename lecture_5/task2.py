try:
    a, b = input("Select numbers: ").split()
    a, b = int(a), int(b)
except ValueError:
    print("Error")
else:
    for i in range (a, b + 1):
        print(i, end=" ")