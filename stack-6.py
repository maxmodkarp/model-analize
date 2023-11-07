def evalRPN(tokens):
    stack = []
    
    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):  
            stack.append(int(token))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            if token == "+":
                result = num1 + num2
            elif token == "-":
                result = num1 - num2
            elif token == "*":
                result = num1 * num2
            else:
                if num1 * num2 < 0 and num1 % num2 != 0:
                    result = (num1 // num2) + 1
                else:
                    result = num1 // num2
            stack.append(result)
    
    return stack[0]

print(evalRPN(["2", "1", "+", "3", "*"])) 
print(evalRPN(["4", "13", "5", "/", "+"]))  
print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])) 
