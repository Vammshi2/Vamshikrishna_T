from collections import deque

def generate_odd_with_queue(n):
    q = deque()
    for i in range(n):
        q.append(2 * i + 1)
    return list(q)

a = int(input("Enter a number: "))
print(", ".join(map(str, generate_odd_with_queue(a))))
