rombs = int(input("Write numbers star - "))
for i in range(0, rombs):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")
#revers
for i in range(rombs, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")