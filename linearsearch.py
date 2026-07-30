a = [10, 20, 30, 40, 50]
x = int(input("Enter number: "))

for i in range(len(a)):
    if a[i] == x:
        print("Found at index", i)
        break
else:
    print("Not Found")
