# Pharmacy Management System

## Overview

The Pharmacy Management System is a comprehensive software solution designed to manage and streamline the operations of a pharmacy. It includes features for inventory management, sales tracking, and customer management. This system aims to simplify pharmacy operations and enhance efficiency.

## Features

- **Inventory Management**: Track and manage medication stock levels, reorder points, and supplier details.
- **Sales Tracking**: Record and manage sales transactions, including payment processing and receipts.
- **Customer Management**: Maintain customer records, track purchase history, and manage customer queries.
- **Reporting**: Generate reports on sales, inventory levels, and other key metrics.
- **User Management**: Support for multiple user roles with different access levels (e.g., admin, pharmacist, cashier).

## Requirements

- Python 3.12 or later
- Flask
- SQLAlchemy
- PyMySQL (or another MySQL connector)
- MySQL server

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/pharmacy-management-system.git
   cd pharmacy-management-system
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Database**

   - Ensure that MySQL server is running and create a database for the application.
   - Update the `config.py` file with your MySQL database connection details:

     ```python
     SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost:3306/pharmacy_inventory'
     ```

5. **Run Migrations**

   Initialize the database schema:

   ```bash
   flask db upgrade
   ```

6. **Run the Application**

   Start the Flask development server:

   ```bash
   flask run
   ```

   The application will be available at `http://127.0.0.1:5000`.

## Entity-Relationship Diagram

The ER diagram below illustrates the relationships between entities in the Pharmacy Management System:

![image](https://github.com/user-attachments/assets/da38b15d-c8b7-43c5-b57c-2c8856db76e1)


## Relational Schema

Here is the relational schema for the Pharmacy Management System:
![image](https://github.com/user-attachments/assets/2a47dc79-d349-44fc-ae98-fb0ab4978ec6)



### Tables

#### 1. **Medications**

| Column         | Type         | Constraints          |
|----------------|--------------|----------------------|
| `med_id`       | INT          | PRIMARY KEY, AUTO_INCREMENT |
| `name`         | VARCHAR(100) | NOT NULL             |
| `description`  | TEXT         |                      |
| `price`        | DECIMAL(10,2) | NOT NULL             |
| `quantity`     | INT          | NOT NULL             |
| `supplier_id`  | INT          | FOREIGN KEY REFERENCES Suppliers(supplier_id) |

#### 2. **Suppliers**

| Column         | Type         | Constraints          |
|----------------|--------------|----------------------|
| `supplier_id`  | INT          | PRIMARY KEY, AUTO_INCREMENT |
| `name`         | VARCHAR(100) | NOT NULL             |
| `contact_info` | TEXT         |                      |

#### 3. **Sales**

| Column         | Type         | Constraints          |
|----------------|--------------|----------------------|
| `sale_id`      | INT          | PRIMARY KEY, AUTO_INCREMENT |
| `sale_date`    | DATE         | NOT NULL             |
| `customer_id`  | INT          | FOREIGN KEY REFERENCES Customers(customer_id) |
| `total_amount` | DECIMAL(10,2) | NOT NULL             |

#### 4. **Sale_Items**

| Column         | Type         | Constraints          |
|----------------|--------------|----------------------|
| `sale_item_id` | INT          | PRIMARY KEY, AUTO_INCREMENT |
| `sale_id`      | INT          | FOREIGN KEY REFERENCES Sales(sale_id) |
| `med_id`       | INT          | FOREIGN KEY REFERENCES Medications(med_id) |
| `quantity`     | INT          | NOT NULL             |
| `price`        | DECIMAL(10,2) | NOT NULL             |

#### 5. **Customers**

| Column         | Type         | Constraints          |
|----------------|--------------|----------------------|
| `customer_id`  | INT          | PRIMARY KEY, AUTO_INCREMENT |
| `name`         | VARCHAR(100) | NOT NULL             |
| `email`        | VARCHAR(100) | UNIQUE               |
| `phone`        | VARCHAR(20)  |                      |

#### 6. **Users**

| Column         | Type         | Constraints          |
|----------------|--------------|----------------------|
| `user_id`      | INT          | PRIMARY KEY, AUTO_INCREMENT |
| `username`     | VARCHAR(50)  | UNIQUE, NOT NULL     |
| `password`     | VARCHAR(255) | NOT NULL             |
| `role`         | VARCHAR(50)  | NOT NULL             |

## Usage

1. **Access the Application**: Open a web browser and navigate to `http://127.0.0.1:5000`.
2. **Log In**: Use the credentials provided to log in. Different user roles will have different access levels.
3. **Manage Inventory**: Add, update, and delete medications and track stock levels.
4. **Process Sales**: Record sales transactions and manage payment processing.
5. **Manage Customers**: View and update customer information and track their purchase history.
6. **Generate Reports**: Access various reports to analyze sales and inventory data.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push to the new branch.
4. Open a pull request detailing your changes.



## Contact

For any questions or issues, please contact:

- **Name**: Manchala Sri Nithin
- **Email**: srinithin17@gmail.com

---
