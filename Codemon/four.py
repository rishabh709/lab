import math

def permutation(num1, num2):
    a = math.factorial(num1+num2)
    b = math.factorial(num1)*math.factorial(num2)

    return a/b


def solve(steps):
    n = steps
    ways=0;
    i = x =0

    while x+1<steps:
        x = 2*i
        ways += permutation(i, steps-x)
        print("ITERATION: ", i, x, ways)
        i+=1

    if(steps==1):
        print(1)
        return 1
    print(ways)

if __name__ == '__main__':
    solve(int(input()))