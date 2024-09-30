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

def valid_user(location):
    data = load_data(location)
    username = input("Enter a username: ").strip()
    password = input("Enter a password: ").strip()

    if "users" in data:
        for user_info in data["users"]:
            if username == user_info["username"] and password == user_info["password"]:
                return True
        print("Invalid Credentials !")
        return False


def view_all_shops(location):
    data = load_data(location)

    for shop in data[location]:
        print("\n----- Shop's Info -----\n")
        print(f"\nShop Name: {shop["shop_name"]} \nShop Id: {shop["shop_id"]}\nShop Owner: {shop["shop_owner"]}\nShop Address: {shop["shop_address"]}\n")
        print("Items: \n")
        for items in shop["shop_items"]:
            print(f"Id: {items['item_id']}, Name: {items['item_name']}, Price: {items['item_price']}, Size: {items['item_size']}, Quantity: {items['item_quantity']}\n")


def place_order(location):
    data = load_data(location)
    shop_name = input("Enter a shop name: ").strip()

    for shop in data[location]:
        if shop_name == shop["shop_name"]:
            item_name = input("Enter item name to purchase: ").strip()

            for item in shop["shop_items"]:
                if str(item["item_name"]) == item_name:
                    print(f"{item_name} is added to your cart and order placed successfully.")
                    return
            print("Item, you are looking for is not available. Please try again")
            return
    print("Shop not found.Please try again !")


def user_operations(location):

    if valid_user(location):

        while True:
            if location in ["etikoppaka", "bobbili", "budithi", "ponduru"]:
                view_all_shops(location)
            else:
                print("Invalid location")

            print("Do you want to place an order ?")
            order = input("Enter yes or no: ")
            if order.lower() == 'yes':
                place_order(location)
            else:
                print("\nYou are exiting, without placing an order.\n")
                break