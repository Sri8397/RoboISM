def double(string): 
    string = list(string)
    finalString = ''.join([str(i)+ str(i) for i in string])
    return finalString

string = input("Enter String: ")
finalString = double(string)
print(f"Output string is {finalString}")