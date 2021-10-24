def my_chain(*collections):
    for i in collections:
        for j in i:
            yield j

collections = my_chain([1, 2, 3], [4, 5, 6], [7, '888', 9])

for j in collections:
    print(j)