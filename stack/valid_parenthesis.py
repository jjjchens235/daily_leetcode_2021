
def isValid(s):
    # we add each opening bracket to a stack
    # if we get to a closing bracket, we pop the stack and make sure they match
    stack = []
    d = {'(': ')', '{': '}', '[': ']'}
    for char in s:
        if char in d.keys():
            stack.append(char)
        else:
            if not stack or d[stack.pop()] != char:
                return False
    return len(stack) == 0

if __name__ == '__main__':
    s = "([)]"
    res = isValid(s)
    print(f'\nres: {res}')
