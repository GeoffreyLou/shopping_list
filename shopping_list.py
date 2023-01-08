import os, json


# Creation of the path variable and boolean on the presence of the file

cur_path = os.path.dirname(__file__)

file_existence = os.path.exists(os.path.join(cur_path, "shopping_list.json"))
file_path = os.path.join(cur_path, "shopping_list.json")


# Creation of the file if it does not exist, with addition of an empty list
# If the file exists but empty, add an empty list

if file_existence == False:
    with open(f"{cur_path}\shopping_list.json", "w") as f:
        json.dump(list(), f, indent = 4)
else:
    try:
        with open(file_path, "r") as f:
            json.load(f)
    except:
        with open(file_path, "w") as f:
            json.dump(list(), f, indent = 4)


# User's menu

menu = """---------------------------------------
Choose from the following 5 options:
1: Add an item to the list
2: Remove an item from the list
3: Show the list
4: Clear the list
5: Exit
Your choice: """


# Open the file and create the list to act on

with open(file_path, "r") as f:
    shopping_list = json.load(f)


# For loop on user's choices

while (choice := input(menu)) != "5":
    if choice == "1":
        add = input("\nWhich item do you want to add to the list? ")
        shopping_list.append(add)
        print(f"\nThe item {add} has been added to the list.\n")
        
    elif choice == "2":
        to_remove = input("\nWhich item do you want to_remove from the list? ")
        if to_remove not in shopping_list:
            print(f"\nThe item {to_remove} is not present in the list.\n")
        else:
            shopping_list.remove(to_remove)
            print(f"\nThe item {to_remove} has been removed from the list.\n")   
            
    elif choice == "3":
        print()
        if shopping_list == []:
            print("The list is empty.")
        else:
            for i, element in enumerate(shopping_list, 1):
                print(i, element)
        print()
        
    elif choice == "4":
        shopping_list.clear()
        print("\nThe list has been cleared.\n")


# End message and save the new list

print("\nYou have just left the program, see you soon!")

with open(file_path, "w") as f:
    json.dump(shopping_list, f, indent = 4)