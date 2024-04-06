## 1. Shopping List Manager
## Create a program that allows users to manage their shopping list. The program should support the following features:
## Adding items to the list
## Removing items from the list
## Displaying the current list
## Checking if an item exists in the list
## Clearing the list

list = []

while True:
    print("1 Add to the list")
    print("2. Remove from the list")
    print("3. View your list")
    choice = int(input("Enter a number: "))

    if choice == 1:
        add = input("Add to the list: ")
        if add == "":
            break
        else:
            list.append(add)
    elif choice == 2:
        print("Your list:", list)
        delete = input("Remove from the list: ")
        if delete in list:
            list.remove(delete)
            print(f"Removed {delete} from list :)")
        else:
            print(f"{delete}'s not in the list")
    elif choice == 3:
        print(list)
