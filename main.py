def Item_Detector(selected_item, selected_item_length):
    with open("Storage.txt", "r") as Storage:
        storage = Storage.read()
    item_length = 0
    item_name = ""
    confirmed_item = ""
    confirmed_item_length = 0
    for i in storage:
        if i.isalpha()  == True:
            item_name += i
            item_length += 1
        if i == " ":
            item_name += i
        if i.isdigit() == True:
            confirmed_item_length = item_length
            confirmed_item = item_name
            item_name = ""
            item_length = 0
            if selected_item == confirmed_item:
                if selected_item_length == confirmed_item_length:
                    return confirmed_item
        else:
            '''print("Iteration:", i)
            print("Item length:", item_length)
            print("Item name:" , item_name)'''
            
            print("Selected length:", selected_item_length)
            print("Confirmed Item Length:", confirmed_item_length)
            print("Selected Item:", selected_item)
            print("Confirmed item:", confirmed_item)
            if selected_item == confirmed_item:
                print(True)
            else:
                print(False)
            print(" ")
            
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
    '''new_item = []
    
    label = input("Please label your item: ")
    quantity = int(input("Please specify the quantity: "))
    
    new_item.append(label)
    new_item.append(quantity)
    
    new_item_finalized = str(new_item)
    
    with open("Storage.txt", "a") as Storage:
        Storage.write(new_item_finalized)

'''
    label = input("Please label your item: ")
    quantity = int(input("Please specify your item: "))

    quantity = str(quantity)

    with open("storage.txt", "w") as storage:
        storage.write(label)
        storage.write(quantity)
        
    with open("storage.txt", "r") as storage:
        storage.read()
        
    return True
        
    return True

def Edit_Change_Label():
    
    with open("Storage.txt", "r") as Storage:
        storage = Storage.read()
    print("You have: ")
    print(storage)
    
    selected_item = input("Please select an item: ")
    item_length = len(selected_item)
    
    confirmed_item = Item_Detector(selected_item, item_length)
   
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
