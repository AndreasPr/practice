def is_integer(token):
    return token.isdigit() or (token[0] == '-' and token[1:].isdigit())

def evaluate_operator(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '==':
        return operand1 == operand2
    elif operator == 'and':
        return operand1 and operand2
    elif operator == 'or':
        return operand1 or operand2

expression = input().split()
stack = []

for token in expression:
    if is_integer(token):
        stack.append(int(token))
    elif token == 'true':
        stack.append(True)
    elif token == 'false':
        stack.append(False)
    else:
        if len(stack) < 2:
            print("SYNTAX ERROR")
            exit()

        operand2 = stack.pop()
        operand1 = stack.pop()

        if type(operand1) != type(operand2):
            print("TYPE ERROR")
            exit()

        if token in ['+', '*', '=='] and type(operand1) is bool:
            print("TYPE ERROR")
            exit()
        
        if token in ['and', 'or'] and type(operand1) is int:
            print("TYPE ERROR")
            exit()

        result = evaluate_operator(token, operand1, operand2)
        stack.append(result)

if len(stack) != 1:
    print("SYNTAX ERROR")
else:
    print(stack[0])
