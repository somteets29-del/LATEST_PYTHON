#inventory
inventory = [
    ["Arduino Starter Kit", "Available"],
    ["Digital Multimeter", "Borrowed"],
    ["Python Crash Course Book", "Available"],
    ["Raspberry Pi 4", "Available"]
]

#borrow function
def borrow_item(item_name):
    found = False

    for item in inventory:
        if item[0].lower() == item_name.lower():
            found = True

            if item[1] == "Available":
                item[1] = "Borrowed"
                print("Item borrowed successfully!")
                return
            else:
                print("The item is not available")
                return

    if not found:
        print("Item not found in inventory")
        print()

#return function             
def return_item(item_name):
    found= False
    
    for item in inventory:
       if item[0].lower() == item_name.lower():
            found = True
            
            if item[1] == "Borrowed":
                item[1] = "Available"
                print("Item returned successfully!")
                return
            elif item[1] == "Available":
                print("Item is on the inventory already!")
                return
                
    if not found:
            print("Item not found in inventory")
            print()

#add function                
def add_item(item_name):
    for item in inventory:
        if item[0].lower() == item_name.lower():
            print("Item is already on the inventory!")
            return
    inventory.append([item_name, "Available"])
    print("Item added Succesfully")
        
    
#start loop                      
while True:
    print("1. View available items")
    print("2. Search for items")
    print("3. Borrow item")
    print("4. Return item")
    print("5. Add new item")
    print("6. Exit")

#ask for choice
    choice = int(input("Enter your choice: "))
    print()
    
#choice 1
    if choice == 1:
        print("The available items are: ")
        available_items = [
        item[0] 
        for item in inventory if item[1] == "Available"
        ]
        for item in available_items:
            print(item)
        print()

#choice 2
    elif choice == 2:
        keyword = input("Enter keyword: ").strip().lower()
       

#search results
        search_results = [
        item[0]
        for item in inventory
        if keyword in item[0].lower()
]
        if search_results:
            print("Search Results:" )
            for result in search_results:
                print(result)
                print()
        else:
                print("No matching items found")
                
#choice 3       
    elif choice == 3:
        item_name = input("Enter item name: ").strip().lower()
        borrow_item(item_name)
        
        
#choice 4
    elif choice == 4:
        item_name = input("Enter item name: ").strip().lower()
        return_item(item_name)

#choice 5
    elif choice == 5:
        item_name = input("Add new item: ")
        add_item(item_name)

#choice 6
    elif choice == 6:
        print("Goodbye!")
        break
    else:
        print("Invalid Selection! Try again")
