def checkPallindrome(word):
    if word == word[-1::-1]:
        return True;

def solve(passwd):
    if len(passwd) < 2:
        print("NO")
    elif checkPallindrome(passwd):
        print("YES")
    else:
        print('NO')
    

if __name__ == '__main__':
    T = int(input())
    newFruits = []

    testCases = [];

    for i in range(T):
        passwd = input()

        testCases.append(passwd);
    
    for password in testCases:
        solve(password)