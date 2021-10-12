import itertools

collections = itertools.chain([1, 2, 3], [4, 5, 6], [7, '888', 9])

def my_chain(collections):
    for i in collections:
        for j in i:
            yield j

for j in collections:
    print(j)