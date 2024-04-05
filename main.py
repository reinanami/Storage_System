def Loading_storage():
   with open("Storage.txt", "r") as Storage:
    lines = Storage.readlines()
   storage =  []

   for l in lines:
    parts = line.strip().split(maxsplit = 1)
    if len(parts) == 2:
        storage.append({'name':parts[0], 'quantity':parts[1]})
    return storage

def Item_detector(selected_item, storage):
    for item in storage:
        if item['name'] == selected_item:
            return item
        return None

            
def Item_Changer(confirmed_item, requested_item):
    
    new_storage = []
        
    item_name = ""
    quantity = ""
    
    for i in storage:
        if i.isalpha() == True:
            item_name += i
        if i == " ":
            item_name = i
        if i.isdigit() == True:
            new_storage.append()
            item_name = ""
        if item_name == confirmed_item:
            item_name = requested_item
            if i.isdigit() == True:
                quantity = i
            
        new_storage.append(item_name)
        new_storage.append(quantity)
            
    with open("Storage.txt", "w") as Storage:
        Storage.write(new_storage)
    

def Create_New():
    new_item = []
    
    label = input("Please label your item: ")
    quantity = int(input("Please specify the quantity: "))
    
    new_item.append(label)
    new_item.append(quantity)
    
    new_item_finalized = str(new_item)
    
    with open("Storage.txt", "a") as Storage:
        Storage.write(new_item_finalized)
        
    return True

def Edit_Change_Label():
    
    with open("Storage.txt", "r") as Storage:
        storage = Storage.read()
    print("You have: ")
    print(storage)
    
    selected_item = input("Please select an item: ")
    item_length = len(selected_item)
    
    storage = Loading_storage()
    confirmed_item = Item_Detector(selected_item, storage)
   
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
