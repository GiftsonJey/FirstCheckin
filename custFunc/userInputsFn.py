def printList(toDolist):
    """this is a function to list all items one by one"""
    for index,item in enumerate(toDolist):
        print(str(index + 1) + ". " + item)