#import function from new file
#with clause
#indesx , enumerate
#for loop with two variables str(index+1)+"."+x+"\n" for index,x in enumerate(toDoList)
from custFunc.userInputsFn import *

with open("files/todo.txt","r") as file:
    toDoList = file.readlines()
toDoList = [ x.strip("\n") for x in toDoList ]
toDoList = [ x.split('.')[1] for x in toDoList ]


if __name__=="__main__":
    while(True):

        printList(toDoList)

        toDoInput = input("To do list: press add or del or exit \n")
        toDoArr = toDoInput.split(' ')
        if (toDoArr[0].upper() == 'ADD'):
            if len(toDoArr) == 1:
                print("For Add keywords , enter the values to be added too \n")
                continue
            toDoList.append(toDoArr[1])
            printList(toDoList)
        elif (toDoArr[0].upper() == 'DEL'):
            if len(toDoArr) == 1:
                print("For Del keywords , enter the values to be added too \n")
                continue
            elif not toDoArr[1].isnumeric():
                print("For Del keyword enter only numeric values")
                continue
            elif (int(toDoArr[1])-1 >= len(toDoList)):
                print("Unable to delete item "+str(toDoArr[1]))
                print("\n")
                continue
            toDoList.pop(int(toDoArr[1])-1)
            printList(toDoList)
        elif (toDoArr[0].upper() == 'EXIT'):
            #wirte to a file
            toDoList = [ str(index+1)+"."+x+"\n" for index,x in enumerate(toDoList) ]
            file = open("files/todo.txt",'w')
            file.writelines(toDoList)
            file.close()
            break
        else:
            print ("Invalid Inputs: Enter valid inputs \n")
            continue



