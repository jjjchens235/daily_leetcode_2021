# Incomplete
def convertToTitle(columnNumber):
    # the last letter in the column name is always the remainder, all preceding letters are based on modulo/26

    # ord returns the integer ascii value of a letter
    # chr returns the character of a int ascii value
    capitals = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    #print(capitals)

    s = ''
    while columnNumber > 26:
        remainder = (columnNumber-1) % 26
        s += capitals[remainder]
        columnNumber = (columnNumber - 1) // 26
        print(columnNumber)

    s += capitals[(columnNumber-1) % 26 ]

    return s[::-1]


if __name__ == '__main__':
    res = convertToTitle(2147483647)
    print(f'\nres: {res}')
