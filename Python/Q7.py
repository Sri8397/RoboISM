def mostFrequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        currFrequency = List.count(i)
        if(currFrequency> counter):
            counter = currFrequency
            num = i
    return num

List = input("Enter array: ").split()
num = mostFrequent(List)
print(num)