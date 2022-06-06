string = list(input("Enter string: "))
sum = 0
for i in string: 
    try:
        sum += int(i)
    except: 
        continue
print(sum)