largest = None
smallest = None
while True:
    n = input("Enter a number: ")
    if n == "done":
        break
    try:
        num=float(n)
        if largest is None:
            largest=num
        elif largest<num:
            largest=num
        if smallest is None:
            smallest=num
        elif smallest>num:
            smallest=num
    except:
        print('Invalid input')
        continue   
print("Maximum is", largest)
print('Minimun is',smallest)