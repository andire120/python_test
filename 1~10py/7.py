a = [int(x) for x in input().split()]
b = a[0]
c = a[1]
d = a[2]

print(int((b+c)%d))
print(int(((b%d) + (c%d))%d))
print(int((b*c)%d))
print(int(((b%d) * (c%d))%d))