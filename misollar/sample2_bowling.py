N = int(input("N = "))
K = int(input("K = "))

list = []
list2 = []

for i in range(N):
    list.append(i+1)

print(list)

while K:
    a = int(input("a = "))
    b = int(input("b = "))
    if a <= b:
        for i in range(a, b+1):
            list2.append(i)
    else:
        for i in range(b, a+1):
            list2.append(i)
    K -= 1
print(list2)
list2 = set(list2)
print(list2)
for i in list:
    if i in list2:
        print(f"*", end = "")
    else:
        print(f"I", end = "")