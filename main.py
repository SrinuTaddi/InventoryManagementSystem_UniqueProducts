from admin import admin_operations
from vendor import vendor_operations
from user import user_operations

def main():
    print("Choose One Option: ")
    print("1.Admin")
    print("2.Vendor")
    print("3.User\n")
    option = int(input("Enter an option: "))

    if option == 1:
        print("\n Locations available are : \n1. Etikoppaka\n2. Ponduru\n3. Bobbili\n4. Budithi\n")
        location = input("Enter a location: ").lower()
        admin_operations(location)
    elif option == 2:    
        print("\n Locations available are : \n1. Etikoppaka\n2. Ponduru\n3. Bobbili\n4. Budithi\n")
        location = input("Enter a location: ").lower()
        vendor_operations(location)
    elif option == 3:  
        print("\n Locations available are : \n1. Etikoppaka\n2. Ponduru\n3. Bobbili\n4. Budithi\n")
        location = input("Enter a location: ").lower()
        user_operations(location)
    else:
        print("Invalid Option")

if __name__ == "__main__":
    main()