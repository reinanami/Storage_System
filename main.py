def Item_Detector(selected_item, selected_item_length): 
    with open("Storage.txt", "r") as Storage:
        storage = Storage.read()
        
    item_length = 0
    item_name = ""
    confirmed_item = ""
    confirmed_item_length = 0
    
    for i in storage:
        if i.isalpha() or i == " ":
            item_name += i
            item_length += 1
        if i == "&":
            confirmed_item_length = item_length
            confirmed_item = item_name
            item_name = ""
            item_length = 0
            if selected_item == confirmed_item:
                if selected_item_length == confirmed_item_length:
                    return confirmed_item

def Check_Alpha(label):
    for i in label:
        if i.isalpha() == False:
            if i != " ":
                print("Your label may not contain symbols or numbers.")
                return 2

def View_Storage():
  with open("Storage.txt", "r") as Storage:
    storage = Storage.read()

    items = storage.split('#')[:-1]
    item_list = []

    for item in items:
       name, quantity = item.split('&')
       item_list.append(name + " " + quantity)            
  print(item_list)
  
  return item_list

def Create_New():
  
    label = input("Please label your item: ")
    check = Check_Alpha(label)
    if check == 2:
        return False
    quantity = int(input("Please specify the quantity: "))
    quantity = str(quantity)
    space = "&"
    tag = "#"
    new_item = (label + space + quantity + tag)
    
    selected_item_length = len(label)
    
    check_for_existing_item = Item_Detector(label, selected_item_length)
    
    if check_for_existing_item == label:
      print("You already have an item named " + label)
      return False
    else:
      with open("Storage.txt", "a") as Storage:
        Storage.write(new_item)
      return True

def Edit_Change_Label():

    print("You have: ")
    
    View_Storage()
    
    selected_item = input("Please select an item: ")
    selected_item_length = len(selected_item)
    
    confirmed_item = Item_Detector(selected_item, selected_item_length)
   
    if selected_item !=  confirmed_item:
        print("Item not found. Please check your spellings or capitalization.")
        return 0
    
    print("Found the item: " + confirmed_item)
   
    print("What would you like to re-label " + confirmed_item + " to?")
    requested_item = input("New label: ")

    check = Check_Alpha(requested_item)
    if check == 2:
        return False

    requested_item_length = len(requested_item)
    check_for_existing_item = Item_Detector(requested_item, requested_item_length)
    if check_for_existing_item == requested_item:
      print("You already have an item named " + requested_item)
      return 0
    else:
        print("Changing label...")
    
    with open("Storage.txt", "r") as Storage:
       storage = Storage.read()

    items = storage.split('#')[:-1]
    updated_storage = ""
    
    for i in items:
        name, quantity = i.split('&')
        if name == confirmed_item:
            updated_storage += requested_item + '&' + quantity + '#'
        else:
            updated_storage += name + '&' + quantity + '#'
              
    with open("Storage.txt", "w") as Storage:
      Storage.write(updated_storage)
    
    return 1
    
    
def Edit_Change_Quantity():
    print("You have: ")
    
    View_Storage()
    
    selected_item = input("Please select an item: ")
    selected_item_length = len(selected_item)
    
    confirmed_item = Item_Detector(selected_item, selected_item_length)
   
    if selected_item !=  confirmed_item:
        print("Item not found. Please check your spellings or capitalization.")
        return 0
    
    print("Found the item: " + confirmed_item)
   
    print("What would you like to re-label " + confirmed_item + "'s quantity to?")
    new_quantity = input("New label: ")
    
    with open("Storage.txt", "r") as Storage:
       storage = Storage.read()

    items = storage.split('#')[:-1]
    updated_storage = ""
    
    for i in items:
        name, quantity = i.split('&')
        if name == confirmed_item:
            updated_storage += name + '&' + new_quantity + '#'
        else:
            updated_storage += name + '&' + quantity + '#'
              
    with open("Storage.txt", "w") as Storage:
      Storage.write(updated_storage)
    
    return 1

def Delete():

    print("You have: ")
    
    View_Storage()
    
    selected_item = input("Please select an item: ")
    selected_item_length = len(selected_item)
    confirmed_item = Item_Detector(selected_item, selected_item_length)
   
    if selected_item !=  confirmed_item:
        print("Item not found. Please check your spellings or capitalization.")
        return 1
    
    print("Found the item: " + confirmed_item)
   
    print("Are you sure that you want to delete: " + confirmed_item + "? (y/n)")
    response = input()
    if response != "y":
        print("Request cancelled.")
        return 1
    
    with open("Storage.txt", "r") as Storage:
       storage = Storage.read()

    items = storage.split('#')[:-1]
    updated_storage = ""
    
    for i in items:
        name, quantity = i.split('&')
        if name == confirmed_item:
            name, quantity = i.split('&')
        else:
            updated_storage += name + '&' + quantity + '#'
              
    with open("Storage.txt", "w") as Storage:
      Storage.write(updated_storage)
    
    return 1
    
def Restart_Storage():
  response = input("Are you sure you want to restart the storage system? (y/n)")
  if response != "y":
      print("The system was not restarted.")
  pernament_response = input("Type 'agree' to confirm restarting the storage system. This action cannot be undone:")
  if pernament_response != "agree":
      print("Cancelled restarting.")
  print("Restarting the system...")
  clear = ""
  
  with open("Storage.txt", "w") as Storage:
      Storage.write(clear)
  return True

#main
print("Welcome to the Storage System!")
while True:
    print("\nType 'Instruction' for the manual.")
    response = input("Command: ")
    if response == "Instruction":
        manual = open("manual.txt")
        print(manual.read())
    elif response == "Create":
        boolean = Create_New()
        if boolean == True:
            print("Wrote item successfully!")
        else:
            print("Error! Something went wrong with the system. Please try again.")
        response = 1
    elif response == "Edit -CL":
        boolean = Edit_Change_Label()
        if boolean == True:
            print("Changed item label successfully.")
        else:
            print("There was an error in changing the label. Please try again.")
    elif response == "Edit -CQ":
        boolean = Edit_Change_Quantity()
        if boolean == True:
            print("Changed item quantity successfully.")
        else:
            print("There was an error in changing the quantity. Please try again.")
    elif response == "Edit -DELETE":
        response = Delete()
    elif response == "Restart":
       Restart_Storage()
       print("Restarted Storage")
    elif response == "View":
        View_Storage()
        response == 1
    elif response == 1:
        print("\n")
