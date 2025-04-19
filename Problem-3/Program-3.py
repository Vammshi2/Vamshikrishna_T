def generate_odd_stack(a):
    stack = []
    limit = a if a % 2 == 1 else a - 1
    for i in range(1, limit + 1, 2):
        stack.append(i)
    return stack[::-1][::-1]  # or simply return stack

a = int(input("Enter a number: "))
print(", ".join(map(str, generate_odd_stack(a))))
