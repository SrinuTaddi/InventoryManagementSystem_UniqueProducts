Unique Products - Inventory Management System

Project Overview: 

The Unique Products Inventory Management System is designed to manage and organize product inventories across multiple shops in four distinct locations: Etikoppaka, Ponduru, Budithi, and Bobbili. 
This system enables the admin to handle shop and product information, manage item requests and returns, and perform CRUD (Create, Read, Update, Delete) operations on inventory data. 
The project is built using Python and utilizes json files for data.

Features: 

        Admin Panel: Manage all tasks, including CRUD operations on shops, products, users, and vendors.
        User Management: Separate login pages for admin, users, and vendors.
        Product Management: Handle inventory data for each shop, including item ID, name, price, size, and quantity.
        Location Management: 
        Four locations with their respective shops:
        Etikoppaka
        Ponduru
        Budithi
        Bobbili
        Vendor System: Vendors manage specific inventory based on location and shop.
        JSON Integration: Shop and product data are stored in location-specific JSON files.
        
JSON Files:

Each location has its own dedicated JSON file, containing information about the shops and the items available:

    etikoppaka.json,
    ponduru.json, 
    budithi.json,
    bobbili.json

The JSON files store the following details:

    Shop Information: Shop ID, name, owner, address, and contact details.
    Item Information: Item ID, name, price, size, and quantity.
Technologies Used:

                  Python: Core programming language for the project.
                  JSON: Used for storing shop and item information.

Usage:

      Admin Login: Admins can log in to manage shops, items, users, and vendors.
      Vendor Login: Vendors can log in to manage shop-specific inventory based on their assigned location.
      User Interaction: Users can log in to browse available products and place item requests or returns.
      
Future Enhancements:

    API Integration: Building APIs with FastAPI for better interaction and third-party integrations.
    Enhanced User Interface: Improve the user interface for easier interaction.
    Reports and Analytics: Adding features to generate reports and track inventory performance over time.
    
Contribution:

Feel free to fork the project, submit pull requests, or raise issues to improve the system.

