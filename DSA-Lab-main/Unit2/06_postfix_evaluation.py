def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()
    operators = {'+', '-', '*', '/'}

    for token in tokens:
        if token not in operators:
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)

    return stack[0]

expressions = [
    "3 4 +",
    "5 1 2 + 4 * + 3 -",
    "2 3 * 4 5 * +"
]

for expr in expressions:
    result = evaluate_postfix(expr)
    print(f"Postfix: {expr} => Result: {result}")
