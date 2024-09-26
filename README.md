# Sales and Inventory Management System

## Overview
This project is a simple Sales and Inventory Management System implemented in Python. It uses a MySQL database to manage product inventory, allowing users to add, update, delete, and display items.

## Features
- Add new items to inventory
- Update existing item prices and quantities
- Delete items from inventory
- Display all items in stock
- Generate bills for customer purchases
- Password protection for admin actions

## Requirements
- Python 3.x
- MySQL Server
- Required Python packages (install via `pip install -r requirements.txt`):
    - `mysql-connector-python`

## How to Run
1. Create an Environment
   python3 -m venv inv
   source /inv/bin/activate
   
2. pip install -r requirements.txt

3. change the MYSQL_USER and MYSQL_PASSWORD in config.py

4. Run the main file
   python main.py

5. For first time user choose option 3



NOTE: 
- Ensure you have Python installed on your system. You can check this by running:
      - python --version
- Make sure you have MySQL installed and running.
- Password of the admin section is *
