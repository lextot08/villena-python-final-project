# villena-python-final-project
Small Business Management System (SBMS)

I. Project Overview
The Small Business Management System (SBMS) is a Python-based desktop application built with the Tkinter GUI library and SQLite for database management. This project helps small business owners efficiently manage their finances and inventories. By allowing users to store, display, add, and delete financial records and inventory data, the system simplifies crucial tasks that help small businesses stay organized and thrive.

Key Features:
-Track and manage budgets with dates.
-Monitor inventory stock levels, product names, and costs.
-Add, display, and delete records from both finance and inventory tables.
-User-friendly interface with navigation buttons for finance and inventory sections.

II. Explanation of Python Concepts, Libraries, and Technologies Used
Python Programming Language:
-The project is written in Python, a versatile language well-suited for building desktop applications. It leverages the power of object-oriented programming, functions, and exception handling to ensure a smooth user experience.

Tkinter:
-Tkinter is the standard GUI library for Python, and it’s used in this project to create windows, buttons, entry fields, and other graphical components for user interaction. Tkinter's simplicity allows for quick and efficient GUI development.

-The application has multiple frames for different functions (Finance and Inventory), and buttons trigger relevant actions (such as adding, displaying, or deleting records).

SQLite:
-SQLite is used for database management in this project. It stores financial and inventory data in two separate tables:
 -tb_sbms for finance data (budget and date).
 -tb_sbms1 for inventory data (product name, stock, and cost).
-The application interacts with SQLite using the sqlite3 library to execute SQL queries for inserting, retrieving, and deleting data.

Pillow (PIL):
-Pillow (PIL) is used for image processing, allowing us to resize and display background images and logos in the GUI. This enhances the aesthetics of the application, providing a better user experience.

Treeview (Tkinter):
-The Treeview widget from Tkinter is used to display data from the SQLite database in a structured tabular format. Users can view financial and inventory records in an easily readable format.

Functions and Event Handling:
-Functions like addFinanceData(), addInventoryData(), deleteData(), and display_data() are defined to handle specific tasks related to adding, displaying, or deleting records. Event handlers link these functions to buttons, allowing users to perform actions in the system.

III. Integration with SDG 8: Decent Work and Economic Growth
This project is aligned with Sustainable Development Goal (SDG) 8: Decent Work and Economic Growth, which focuses on promoting inclusive and sustainable economic growth, productive employment, and decent work for all.

Promoting Economic Growth: By enabling small businesses to track their budgets and manage their inventories, the system helps businesses optimize resources and make data-driven decisions, which supports economic growth.

Decent Work: The application indirectly contributes to creating more productive, organized work environments for small businesses. By managing finances and inventory more efficiently, business owners can improve their operations, leading to better job security and working conditions for employees.

Sustainability: The ability to track inventory and costs ensures that businesses can avoid wasteful practices, reduce expenses, and ultimately foster sustainable economic growth.

Supporting Entrepreneurship: By providing tools for financial and inventory management, the system empowers entrepreneurs to operate more effectively, contributing to job creation and local economic development.

IV. Instructions for Running the Program
Before running the program, ensure that the following Python libraries are installed on your system:

tkinter (usually comes pre-installed with Python)
sqlite3 (also comes pre-installed with Python)
Pillow (for image processing)

Running the Program:
1. Clone or download the repository to your local machine.
2. Ensure that the required images (like the background image and logo) are in the correct path or adjust the paths in the code accordingly.
3. Open a terminal or command prompt and navigate to the project folder.
4. Run the Python script:

The program will launch a graphical user interface where you can interact with the Small Business Management System.
