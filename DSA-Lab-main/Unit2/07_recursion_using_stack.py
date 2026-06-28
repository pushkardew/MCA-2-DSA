def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_with_stack(n):
    call_stack = []
    result = 1

    current = n
    while current > 1:
        call_stack.append(current)
        current -= 1

    print("Simulated call stack (top to bottom):", call_stack[::-1])

    while call_stack:
        result *= call_stack.pop()

    return result

n = 5
print(f"Factorial of {n} using recursion: {factorial_recursive(n)}")
print(f"Factorial of {n} using stack simulation: {factorial_with_stack(n)}")
