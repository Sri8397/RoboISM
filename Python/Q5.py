def findDuplicate(lst): 
    for i in range(len(lst)): 
        if lst.count(lst[i]) > 1: 
            return lst[i]

lst = [int(num) for num in input("Enter an array which contains an duplicate: ").split()]
duplicate = findDuplicate(lst)
print(f"Duplicate number is {duplicate}")