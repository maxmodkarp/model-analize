def isValid(s):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if not stack or stack.pop() != brackets[char]:
                return False
    
    return not stack

print(isValid("()")) 
print(isValid("()[]{}"))  
print(isValid("(]"))  
