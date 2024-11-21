a,b = map(int,input().split())
c = int(input())
d = a * 60 + b + c

if d < 0:
    d += 24 * 60

a = d // 60
b = d % 60

if a > 24:
    a -= 24
    
elif a == 24:
    a = 0

print(a, b)