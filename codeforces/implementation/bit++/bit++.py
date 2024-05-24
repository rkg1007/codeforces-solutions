# https://codeforces.com/problemset/problem/282/A

def findFinalVal(noOfStatements, statements):
    currVal = 0
    incrementStatements = ['X++', '++X']
    for statement in statements:
        if statement in incrementStatements:
            currVal += 1
        else:
            currVal -= 1
    return currVal

def main():
    noOfStatements = int(input())
    statements = []
    for _ in range(noOfStatements):
        statement = input()
        statements.append(statement)
    finalVal = findFinalVal(noOfStatements, statements)
    print(finalVal)

if __name__ == '__main__':
    main()