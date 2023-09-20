list1 = []
for x in range(10):
    num = int(input("enter a number: "))
    list1.append(num)


maximum = 0
for x in list1:
    if x > maximum:
        maximum = x

print(f"the biggest number is: {maximum}")