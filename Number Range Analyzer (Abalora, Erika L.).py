num=eval(input("Enter a number: "))
smallest=num
largest=num

while num!=0:
    num = eval(input("Enter a number (0 to stop): "))
    if num>largest:
        largest=num
    elif num<smallest and num!=0:
        smallest=num
    else:
        print("End of the program")
        break

print("The largest number is ", largest)
print("The smallest number is ", smallest)
print("The difference between the largest and smallest is ", largest - smallest)
