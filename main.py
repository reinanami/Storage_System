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

def View_Storage():
  with open("Storage.txt", "r") as Storage:
    storage = Storage.read()
    
    item_name = ""
    item_list = []
    
    for i in storage:
      if i == "&":
        item_list.append(item_name)
        item_name = ""
        item_length = 0
      else:
        item_name += i
            
  print(item_list)
  
  return item_list
     
def Item_Changer(confirmed_item, requested_item):
    with open("Storage.txt", "r") as Storage:
      storage = Storage.read()

    item_name = ""
    quantity = 0
    write_to_storage = ""
    space = "&"
    
    for i in storage:
        if i.isalpha()  or i == " ":
            item_name += i
        if i.isdigit():
          quantity += i
        elif i == space:
            if item_name.strip() == confirmed_item:
              write_to_storage = (requested_item + space + selected_quantity + space)
            else:
              write_to_storage = (item_name + space + selected_quantity + space)
              
    with open("Storage.txt", "w") as Storage:
      Storage.write(write_to_storage)
      
    return True
    
def Create_New():
  
    label = input("Please label your item: ")
    quantity = int(input("Please specify the quantity: "))
    quantity = str(quantity)
    space = ("&")
    new_item = (label + space + quantity + space)
    
    with open("Storage.txt", "a") as Storage:
        Storage.write(new_item)
        
    return True

def Edit_Change_Label():
    
    with open("Storage.txt", "r") as Storage:
        storage = Storage.read()
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
    changed_label = input("New label: ")
    
    return 1
    
    
def Edit_Change_Quantity():
    return True

def Delete():
    return True
    
def Restart_Storage():
    return True

#main
print("Welcome to the Storage System!")
while True:
    print("Type --H for help.")
    response = input("Command: ")
    if response == "--H":
        manual = open("manual.txt")
        print(manual.read())
    elif response == "Create":
        boolean = Create_New()
        if boolean == True:
            print("Wrote item successfully!")
        else:
            print("Error! Something went wrong with the system.")
        response = 1
    elif response == "Edit -CL":
        boolean = Edit_Change_Label()
        if boolean == True:
            print("Changed item label successfully.")
        else:
            print("There was an error in changing the label. Please try again.")
    elif response == 1:
        print()
    else:
        print("Error! You may want to type --H for help.")
