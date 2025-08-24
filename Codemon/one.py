def solve(n, s):
    sum = 0
    for i in range(n):
        sum = sum + 1 + i

    if(s==0):
        print(-1)
        return
    print(sum-s)
    return sum-s






if __name__ == '__main__':
    n = int(input())
    s = int(input())
    solve(n, s)
