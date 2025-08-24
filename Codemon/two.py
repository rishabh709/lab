def spoil(fruits):
    spoil_fruits = []
    for f in fruits:
        if(f-1>0):
            spoil_fruits.append(f-1);
    return spoil_fruits


def solve(fruits):
    sorted(fruits)
    harvest = 0
    while len(fruits)!=0:
        harvest += fruits.pop()
        fruits = spoil(fruits)
    print(harvest)
    

if __name__ == '__main__':
    T = int(input())
    newFruits = []

    for i in range(T):
        N = int(input())

        fruits = input()
        fruits = fruits.split(" ")
        for f in fruits:
            newFruits.append(int(f))
        solve(newFruits)