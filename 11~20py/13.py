a = int(input())
b = []

for x in range(1, a+1):
    a, b = [int(x) for x in input().split()]
    print(f"Case #{x}: {a} + {b} = {a+b}")
