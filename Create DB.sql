CREATE DATABASE artifact_db;

CREATE TABLE Regions (
    region_id INT NOT NULL,
    name VARCHAR(25) NOT NULL,
    manager_id INT,
    PRIMARY KEY (region_id)
);

CREATE TABLE States (
    iso CHAR(2) NOT NULL,
    name VARCHAR(25) NOT NULL,
    region_id INT NOT NULL,
    PRIMARY KEY (iso),
    FOREIGN KEY (region_id) REFERENCES Regions(region_id)
);

CREATE TABLE Addresses (
    address_id INT NOT NULL AUTO_INCREMENT,
    street VARCHAR(75) NOT NULL,
    city VARCHAR(25) NOT NULL,
    zip CHAR(5) NOT NULL,
    state CHAR(2) NOT NULL,
    PRIMARY KEY (address_id),
    FOREIGN KEY (state) REFERENCES States(iso)
);

CREATE TABLE Customers (
    customer_id INT NOT NULL AUTO_INCREMENT,
    f_name VARCHAR(25) NOT NULL,
    l_name VARCHAR(25) NOT NULL,
    phone VARCHAR(15),
    email VARCHAR(50) UNIQUE NOT NULL,
    password CHAR(20) NOT NULL,
    kind VARCHAR(8) NOT NULL,
    address_id INT,
    PRIMARY KEY (customer_id),
    FOREIGN KEY (address_id) REFERENCES Addresses(address_id)
);

CREATE TABLE Business_Customer (
    customer_id INT UNIQUE NOT NULL,
    business_name VARCHAR(50) NOT NULL,
    category VARCHAR(25),
    gross_annual_income INT,
    PRIMARY KEY (customer_id),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    ON DELETE CASCADE
);

CREATE TABLE Home_Customer (
    customer_id INT UNIQUE NOT NULL,
    marriage_status VARCHAR(10),
    gender VARCHAR(8),
    dob DATE,
    income INT,
    PRIMARY KEY (customer_id),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
	ON DELETE CASCADE
);

CREATE TABLE Stores (
    store_id INT NOT NULL AUTO_INCREMENT,
    salesperson_num INT,
    manager_id INT,
    region_id INT NOT NULL,
	PRIMARY KEY (store_id),
    FOREIGN KEY (region_id) REFERENCES Regions(region_id)
);

CREATE TABLE Job_Titles (
    title_id INT NOT NULL AUTO_INCREMENT,
    job_title VARCHAR(25) NOT NULL,
    salary DECIMAL(12,2) NOT NULL,
    PRIMARY KEY (title_id)
);

CREATE TABLE Salespersons (
    salesperson_id INT NOT NULL AUTO_INCREMENT,
    f_name VARCHAR(25) NOT NULL,
    l_name VARCHAR(25) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password CHAR(20),
    job_title_id INT NOT NULL,
    address_id INT,
    store_id INT NOT NULL,
    PRIMARY KEY (salesperson_id),
    FOREIGN KEY (address_id) REFERENCES Addresses(address_id),
    FOREIGN KEY (store_id) REFERENCES Stores(store_id),
    FOREIGN KEY (job_title_id) REFERENCES Job_Titles(title_id)
);

ALTER TABLE Regions
ADD FOREIGN KEY (manager_id) REFERENCES Salespersons(salesperson_id);

ALTER TABLE Stores
ADD FOREIGN KEY (manager_id) REFERENCES Salespersons(salesperson_id);

CREATE TABLE Product_Type (
	product_type_id INT NOT NULL AUTO_INCREMENT,
    type VARCHAR(45) NULL,
    PRIMARY KEY (product_type_id)
);

CREATE TABLE Products (
	product_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(45) NOT NULL,
    inventory INT NOT NULL,
    price DECIMAL(12,2) NOT NULL,
    product_type_id INT NULL,
    PRIMARY KEY (product_id),
    FOREIGN KEY (product_type_id) REFERENCES Product_Type(product_type_id)
);

CREATE TABLE Product_Description (
	product_id INT UNIQUE NOT NULL,
	product_description VARCHAR(250) NULL,
    image_path VARCHAR(200) NULL,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
    ON DELETE CASCADE
);

CREATE TABLE Transactions (
    order_num INT NOT NULL AUTO_INCREMENT,
    order_date DATETIME,    
    customer_id INT NOT NULL,
    salesperson_id INT NOT NULL,    
    PRIMARY KEY (order_num),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    ON DELETE CASCADE,
    FOREIGN KEY (salesperson_id) REFERENCES Salespersons(salesperson_id)    
);

CREATE TABLE Cart_Items (
    item_id INT NOT NULL AUTO_INCREMENT,
    created_date DATETIME NOT NULL,
    quantity INT NOT NULL,
    cart_id INT NOT NULL,
    product_id INT NOT NULL,
    PRIMARY KEY (item_id),
    FOREIGN KEY (cart_id) REFERENCES Transactions(order_num)
    ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
    ON DELETE CASCADE
);