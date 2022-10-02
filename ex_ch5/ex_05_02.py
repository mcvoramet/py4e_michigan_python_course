largest = None
smallest = None
np = []
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        number = int(num)
        np.append(number)
    except:
        print("Invalid input")
        continue
for value in np:
    if largest is None :
        largest = value
    elif value > largest :
        largest = value

for value in np:
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value

print("Maximum is", largest)
print("Minimum is", smallest)
