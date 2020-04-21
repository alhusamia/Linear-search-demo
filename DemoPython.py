def search(list,num):
    for i in range(len(list)):
        if num == list[i]:
            print("You find the number ... the index of it ",i)
            break
    else:
        print("NOt found !!")




list=[1,2,56,87,9,100,9]
print(list)
num = int(input("Enter the number that you are searching for :"))

search(list,num)