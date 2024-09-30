import json

def load_data(location):
    json_file = f"{location}.json"
    with open(json_file, "r") as file:
        data = json.load(file)
    return data

def save_data(data, location):
    json_file = f"{location}.json"
    with open(json_file, "w") as f:
        data = json.dump(data, f, indent=4)

def valid_vendor(location):
    data = load_data(location)
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    if "vendor" in data:
        for vendor_info in data["vendor"]:
            if username == vendor_info["username"] and password == vendor_info["password"]:
                return True
        print("Invalid Credentials !")


def view_all_shops(location):
    data = load_data(location)

    for shop in data[location]:
        print("\n----- Shop's Info -----\n")
        print(f"\nShop Name: {shop["shop_name"]} \nShop Id: {shop["shop_id"]}\nShop Owner: {shop["shop_owner"]}\nShop Address: {shop["shop_address"]}\n")
        print("Items: \n")
        for items in shop["shop_items"]:
            print(f"Id: {items['item_id']}, Name: {items['item_name']}, Price: {items['item_price']}, Size: {items['item_size']}, Quantity: {items['item_quantity']}\n")
                

def add_new_item(location):
    data = load_data(location)
    shop_name = input("Enter a shop name: ")

    for shop in data[location]:

        if shop["shop_name"] == shop_name:
            
            item_id = input("Enter item id: ")
            item_name = input("Enter item name: ")
            item_price = input("Enter item price: ")
            item_size = input("Enter item size: ")
            item_quantity = input("Enter item quantity: ")
            new_item = {
                "item_id": item_id,
                "item_name" : item_name,
                "item_price" : item_price,
                "item_size" : item_size,
                "item_quantity" : item_quantity
            }
            shop["shop_items"].append(new_item)
            save_data(data, location)
            print(f"'{item_name}' is added to the '{shop_name}' shop.")
            return 
    print("Shop not found. Please try again.")
            

def delete_item(location):
    data = load_data(location)
    shop_name = input("Enter a shop name: ").strip()

    for shop in data[location]:
        if shop["shop_name"] == shop_name:
            item_id = input("Enter item id: ").strip()

            for item in shop["shop_items"]:
                if str(item["item_id"]) == item_id:
                    shop["shop_items"].remove(item)
                    save_data(data, location)
                    print(f"Item id : {item_id} is deleted from the items list.")
                    return
            print("Item not found. Please try again.")
            return
    print("Shop not found. Please try again.")
    
def vendor_operations(location):

    if valid_vendor(location):

        print("\nYour abilities: \n")
        print("1. View All Shops")
        print("2. Add items")
        print("3. Delete items")
        print("4. Exit")

        while True:
            option = input("Choose an option: ")
            if option == "1":
                view_all_shops(location)
            elif option == "2":
                add_new_item(location)
            elif option == "3":
                delete_item(location)
            elif option == "4":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Enter a valid option.")
