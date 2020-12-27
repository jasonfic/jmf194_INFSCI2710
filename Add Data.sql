INSERT INTO `product_type` (`type`) VALUES ('Wearables');
INSERT INTO `product_type` (`type`) VALUES ('Decorations');
INSERT INTO `product_type` (`type`) VALUES ('Functional');
INSERT INTO `product_type` (`type`) VALUES ('Pets');
INSERT INTO `product_type` (`type`) VALUES ('Body Modifications');
INSERT INTO `product_type` (`type`) VALUES ('Games');
INSERT INTO `product_type` (`type`) VALUES ('Books');

INSERT INTO Products (name, inventory, price, product_type_id)
VALUES ('Wizard Hat', 250, 9.99, 1);
INSERT INTO Product_Description (product_id, product_description, image_path)
VALUES (1, 'A lovely hat that will ensure you cast spells in style!', '../static/images/wizard_hat.jpg');
INSERT INTO Products (name, inventory, price, product_type_id)
VALUES ('Suit of Armor', 75, 625.00, 1);
INSERT INTO Product_Description (product_id, product_description, image_path)
VALUES (2, 'Wear this into battle and come out without a scratch!', '../static/images/armor.jpg');
INSERT INTO Products (name, inventory, price, product_type_id)
VALUES ('Invisibility Cloak', 20, 14999.99, 1);
INSERT INTO Product_Description (product_id, product_description, image_path)
VALUES (3, 'Have you ever wanted to be a fly on the wall? With this product, you will be even more discrete than that!', '../static/images/invisibility_cloak.jpg');
INSERT INTO Products (name, inventory, price, product_type_id)
VALUES ('Magic Robes', 150, 59.99, 1);
INSERT INTO Product_Description (product_id, product_description, image_path)
VALUES (4, 'With these graceful robes, casting spells has never been more confortable.', '../static/images/wizard_robes.png');
INSERT INTO Products (name, inventory, price, product_type_id)
VALUES ('The One Ring', 1, 9999999999.99, 1);
INSERT INTO Product_Description (product_id, product_description, image_path)
VALUES (5, 'NOTICE: Enchantr is not legally liable if this product is used to take over the world for evil.', '../static/images/one_ring.jpg');
INSERT INTO Products (name, inventory, price, product_type_id)
VALUES ('Plague Doctor Mask', 200, 34.99, 1);
INSERT INTO Product_Description (product_id, product_description, image_path)
VALUES (6, 'Global pandemic? We gotcha covered.', '../static/images/plague_mask.jpg');

INSERT INTO Products (name, inventory, price, product_type_id)
VALUES ('Dragon Egg', 3, 49999999.99, 2);
INSERT INTO Product_Description (product_id, product_description, image_path)
VALUES (7, 'NOTICE: Enchantr is not legal liable if these somehow hatch and the owner uses them to burn down a city.', '../static/images/dragon_eggs.jpg');
INSERT INTO Products (name, inventory, price, product_type_id)
VALUES ('Orc Skull', 100, 19.99, 2);
INSERT INTO Product_Description (product_id, product_description, image_path)
VALUES (8, 'Use this as a warning to your enemies that you are not to be messed with!', '../static/images/orc_skull.jpg');
INSERT INTO Products (name, inventory, price, product_type_id)
VALUES ('Sword', 200, 74.99, 2);
INSERT INTO Product_Description (product_id, product_description, image_path)
VALUES (9, 'Simple. Effecient. Classic. Lovely over a fireplace!', '../static/images/sword.jpeg');
INSERT INTO Products (name, inventory, price, product_type_id)
VALUES ('Shrunken Head', 300, 9.99, 2);
INSERT INTO Product_Description (product_id, product_description, image_path)
VALUES (10, 'One thing is for sure, this will be a conversation starter!', '../static/images/shrunken_head.jpg');

INSERT INTO Products (name, inventory, price, product_type_id)
VALUES ('Magic Wand', 500, 34.99, 3);
INSERT INTO Product_Description (product_id, product_description, image_path)
VALUES (11, 'A must-have for every aspiring wizard.', '../static/images/magic_wand.jpg');
INSERT INTO Products (name, inventory, price, product_type_id)
VALUES ('Flying Broomstick', 250, 120.00, 3);
INSERT INTO Product_Description (product_id, product_description, image_path)
VALUES (12, 'It can be used for a bit more than cleaning!', '../static/images/flying_broomstick.jpg');
INSERT INTO Products (name, inventory, price, product_type_id)
VALUES ('Flying Carpet', 100, 175.00, 3);
INSERT INTO Product_Description (product_id, product_description, image_path)
VALUES (13, 'We can show you the world!', '../static/images/flying_carpet.jpg');
INSERT INTO Products (name, inventory, price, product_type_id)
VALUES ('Genie Lamp', 10, 24999.99, 3);
INSERT INTO Product_Description (product_id, product_description, image_path)
VALUES (14, 'Do not even TRY to wish for more wishes.', '../static/images/genie_lamp.jpg');

INSERT INTO Products (name, inventory, price, product_type_id)
VALUES ('Unicorn', 12, 75000000.00, 4);
INSERT INTO Product_Description (product_id, product_description, image_path)
VALUES (15, 'In case regular horses are too plain for you.', '../static/images/unicorn.jpg');
INSERT INTO Products (name, inventory, price, product_type_id)
VALUES ('Vampire Bat', 75, 125.00, 4);
INSERT INTO Product_Description (product_id, product_description, image_path)
VALUES (16, 'We cannot confirm or deny that this will turn into an actual vampire.', '../static/images/vampire_bat.jpg');
INSERT INTO Products (name, inventory, price, product_type_id)
VALUES ('Direwolf', 25, 20000.00, 4);
INSERT INTO Product_Description (product_id, product_description, image_path)
VALUES (17, 'Get yourself a companion for life! No guarantees that you can control them with your mind, though.', '../static/images/direwolf.jpg');
INSERT INTO Products (name, inventory, price, product_type_id)
VALUES ('Griffin', 2, 90000000.00, 4);
INSERT INTO Product_Description (product_id, product_description, image_path)
VALUES (18, '50% lion. 50% eagle. 100% cool.', '../static/images/griffin.jpg');
INSERT INTO Products (name, inventory, price, product_type_id)
VALUES ('Messenger Owl', 50, 300.00, 4);
INSERT INTO Product_Description (product_id, product_description, image_path)
VALUES (19, 'Is sending text messages just too fast and efficient for you?', '../static/images/messenger_owl.jpg');

INSERT INTO Products (name, inventory, price, product_type_id)
VALUES ('Fairy Wings', 35, 525.00, 5);
INSERT INTO Product_Description (product_id, product_description, image_path)
VALUES (20, 'Fly fabulously.', '../static/images/fairy_wings.png');
INSERT INTO Products (name, inventory, price, product_type_id)
VALUES ('Dragon Tail', 21, 1200.00, 5);
INSERT INTO Product_Description (product_id, product_description, image_path)
VALUES (21, 'Will you be able to sit comfortably? No. But will you look cool? Eh, it is subjective.', '../static/images/dragon_tail.jpg');
INSERT INTO Products (name, inventory, price, product_type_id)
VALUES ('Arcane Tattoos', 500, 15.00, 5);
INSERT INTO Product_Description (product_id, product_description, image_path)
VALUES (22, 'Temporary tattoos that glow and may grant magic powers. Use responsibly.', '../static/images/arcane_tattoos.jpg');
INSERT INTO Products (name, inventory, price, product_type_id)
VALUES ('Cyclops Eye', 28, 150.00, 5);
INSERT INTO Product_Description (product_id, product_description, image_path)
VALUES (23, 'Sometimes, one eye is better than two.', '../static/images/cyclops_eye.jpg');

INSERT INTO Products (name, inventory, price, product_type_id)
VALUES ('Ouija Board', 1250, 19.99, 6);
INSERT INTO Product_Description (product_id, product_description, image_path)
VALUES (24, 'The spirits of the dead surprisingly never shut up.', '../static/images/ouija_board.jpg');
INSERT INTO Products (name, inventory, price, product_type_id)
VALUES ('Bloody Mary Mirror', 300, 9.99, 6);
INSERT INTO Product_Description (product_id, product_description, image_path)
VALUES (25, 'Feeling lonely? Say Bloody Mary three times in front of this product and solve that problem instantly!', '../static/images/bloody_mary.jpg');
INSERT INTO Products (name, inventory, price, product_type_id)
VALUES ('Gwent', 2000, 4.99, 6);
INSERT INTO Product_Description (product_id, product_description, image_path)
VALUES (26, 'A thrilling and strategic card game that pits two magical armies against each other.', '../static/images/gwent.jpg');

INSERT INTO Products (name, inventory, price, product_type_id)
VALUES ('Necronomicon', 1, 100000000.00, 7);
INSERT INTO Product_Description (product_id, product_description, image_path)
VALUES (27, 'NOTICE: Enchantr is not legally liable if an owner of this product attempt to read any unpronouncable words from this book out loud.', '../static/images/necronomicon.jpg');
INSERT INTO Products (name, inventory, price, product_type_id)
VALUES ('Spellbook (USED)', 99, 14.99, 7);
INSERT INTO Product_Description (product_id, product_description, image_path)
VALUES (28, 'A bit yellow and worn, but this book still has some tricks up its sleeve.', '../static/images/spellbook.jpg');

INSERT INTO Job_Titles (title_id, job_title, salary)
VALUES (1, 'Manager', 125000.00);
INSERT INTO Job_Titles (title_id, job_title, salary)
VALUES (2, 'Salesperson', 60000.00);
INSERT INTO Job_Titles (title_id, job_title, salary)
VALUES (3, 'Intern', 30000.00);

INSERT INTO Regions (region_id, name)
VALUES (1, 'Northeast');
INSERT INTO Regions (region_id, name)
VALUES (2, 'Southeast');
INSERT INTO Regions (region_id, name)
VALUES (3, 'Midwest');
INSERT INTO Regions (region_id, name)
VALUES (4, 'Southwest');
INSERT INTO Regions (region_id, name)
VALUES (5, 'West');

INSERT INTO States (iso, name, region_id)
VALUES ('CT', 'Connecticut', 1);
INSERT INTO States (iso, name, region_id)
VALUES ('ME', 'Maine', 1);
INSERT INTO States (iso, name, region_id)
VALUES ('MA', 'Massachusetts', 1);
INSERT INTO States (iso, name, region_id)
VALUES ('NH', 'New Hampshire', 1);
INSERT INTO States (iso, name, region_id)
VALUES ('NY', 'New York', 1);
INSERT INTO States (iso, name, region_id)
VALUES ('NJ', 'New Jersey', 1);
INSERT INTO States (iso, name, region_id)
VALUES ('PA', 'Pennsylvania', 1);
INSERT INTO States (iso, name, region_id)
VALUES ('RI', 'Rhode Island', 1);
INSERT INTO States (iso, name, region_id)
VALUES ('VT', 'Vermont', 1);
INSERT INTO States (iso, name, region_id)
VALUES ('DE', 'Delaware', 2);
INSERT INTO States (iso, name, region_id)
VALUES ('DC', 'District of Columbia', 2);
INSERT INTO States (iso, name, region_id)
VALUES ('MD', 'Maryland', 2);
INSERT INTO States (iso, name, region_id)
VALUES ('SC', 'South Carolina', 2);
INSERT INTO States (iso, name, region_id)
VALUES ('VA', 'Virginia', 2);
INSERT INTO States (iso, name, region_id)
VALUES ('WV', 'West Virginia', 2);
INSERT INTO States (iso, name, region_id)
VALUES ('NC', 'North Carolina', 2);
INSERT INTO States (iso, name, region_id)
VALUES ('MS', 'Mississippi', 2);
INSERT INTO States (iso, name, region_id)
VALUES ('AR', 'Arkansas', 2);
INSERT INTO States (iso, name, region_id)
VALUES ('TN', 'Tennessee', 2);
INSERT INTO States (iso, name, region_id)
VALUES ('FL', 'Florida', 2);
INSERT INTO States (iso, name, region_id)
VALUES ('GA', 'Georgia', 2);
INSERT INTO States (iso, name, region_id)
VALUES ('AL', 'Alabama', 2);
INSERT INTO States (iso, name, region_id)
VALUES ('KY', 'Kentucky', 2);
INSERT INTO States (iso, name, region_id)
VALUES ('LA', 'Louisiana', 2);
INSERT INTO States (iso, name, region_id)
VALUES ('IL', 'Illinois', 3);
INSERT INTO States (iso, name, region_id)
VALUES ('IN', 'Indiana', 3);
INSERT INTO States (iso, name, region_id)
VALUES ('IA', 'Iowa', 3);
INSERT INTO States (iso, name, region_id)
VALUES ('KS', 'Kansas', 3);
INSERT INTO States (iso, name, region_id)
VALUES ('MI', 'Michigan', 3);
INSERT INTO States (iso, name, region_id)
VALUES ('MN', 'Minnesota', 3);
INSERT INTO States (iso, name, region_id)
VALUES ('MO', 'Missouri', 3);
INSERT INTO States (iso, name, region_id)
VALUES ('NE', 'Nebraska', 3);
INSERT INTO States (iso, name, region_id)
VALUES ('ND', 'North Dakota', 3);
INSERT INTO States (iso, name, region_id)
VALUES ('OH', 'Ohio', 3);
INSERT INTO States (iso, name, region_id)
VALUES ('SD', 'South Dakota', 3);
INSERT INTO States (iso, name, region_id)
VALUES ('WI', 'Wisconsin', 3);
INSERT INTO States (iso, name, region_id)
VALUES ('AZ', 'Arizona', 4);
INSERT INTO States (iso, name, region_id)
VALUES ('NM', 'New Mexico', 4);
INSERT INTO States (iso, name, region_id)
VALUES ('OK', 'Oklahoma', 4);
INSERT INTO States (iso, name, region_id)
VALUES ('TX', 'Texas', 4);
INSERT INTO States (iso, name, region_id)
VALUES ('MT', 'Montana', 5);
INSERT INTO States (iso, name, region_id)
VALUES ('WY', 'Wyoming', 5);
INSERT INTO States (iso, name, region_id)
VALUES ('CO', 'Colorado', 5);
INSERT INTO States (iso, name, region_id)
VALUES ('ID', 'Idaho', 5);
INSERT INTO States (iso, name, region_id)
VALUES ('UT', 'Utah', 5);
INSERT INTO States (iso, name, region_id)
VALUES ('NV', 'Nevada', 5);
INSERT INTO States (iso, name, region_id)
VALUES ('WA', 'Washington', 5);
INSERT INTO States (iso, name, region_id)
VALUES ('OR', 'Oregon', 5);
INSERT INTO States (iso, name, region_id)
VALUES ('CA', 'California', 5);
INSERT INTO States (iso, name, region_id)
VALUES ('AK', 'Alaska', 5);
INSERT INTO States (iso, name, region_id)
VALUES ('HI', 'Hawaii', 5);

INSERT INTO Customers (f_name, l_name, phone, email, password, kind)
VALUES ('Jason', 'Ficorilli', '724-328-3304', 'jmf194@pitt.edu', 'Password1', 'Personal');
INSERT INTO Addresses (street, city, state, zip)
VALUES('123 Street Ave', 'Pittsburgh', 'PA', '15213');
UPDATE Customers SET address_id=1 WHERE customer_id=1;
INSERT INTO Home_Customer (customer_id, gender, dob, income)
VALUES (1, 'Male', STR_TO_DATE('02/26/1998','%m/%d/%Y'), '50000.00');
INSERT INTO Customers (f_name, l_name, phone, email, password, kind)
VALUES ('Brenna', 'Schroter', '247-283-3043', 'bks39@pitt.edu', 'Password2', 'Personal');
INSERT INTO Addresses (street, city, state, zip)
VALUES('321 Road St', 'Chicago', 'IL', '60608');
UPDATE Customers SET address_id=2 WHERE customer_id=2;
INSERT INTO Home_Customer (customer_id, gender, dob, income)
VALUES (2, 'Female', STR_TO_DATE('11/16/1997','%m/%d/%Y'), '60000.00');
INSERT INTO Customers (f_name, l_name, phone, email, password, kind)
VALUES ('Neha', 'Shah', '427-832-4303', 'nes95@pitt.edu', 'Password3', 'Personal');
INSERT INTO Addresses (street, city, state, zip)
VALUES('231 Avenue Ln', 'Los Angeles', 'CA', '90011');
UPDATE Customers SET address_id=3 WHERE customer_id=3;
INSERT INTO Home_Customer (customer_id, gender, dob, income)
VALUES (3, 'Female', STR_TO_DATE('07/16/1996','%m/%d/%Y'), '70000.00');

INSERT INTO Customers (f_name, l_name, email, password, kind)
VALUES ('Bobson', 'Dugnutt', 'duggybob@email.com', 'Password4', 'Business');
INSERT INTO Business_Customer (customer_id, business_name, category, gross_annual_income)
VALUES (4, 'Ye Olde Trinket Shoppe', 'Retail', 3000000.00);
INSERT INTO Addresses (street, city, state, zip)
VALUES('312 Lane Dr', 'Atlanta', 'GA', '30311');
UPDATE Customers SET address_id=4 WHERE customer_id=4;

INSERT INTO Customers (f_name, l_name, email, password, kind)
VALUES ('Toby', 'Gunch', 'tobytobe@email.com', 'Password5', 'Business');
INSERT INTO Business_Customer (customer_id, business_name, category, gross_annual_income)
VALUES (5, 'Toby\'s House of Horrors', 'Retail', 2200000.00);
INSERT INTO Addresses (street, city, state, zip)
VALUES('312 Drive Rd', 'Phoenix', 'AZ', '85005');
UPDATE Customers SET address_id=5 WHERE customer_id=5;

INSERT INTO Customers (f_name, l_name, email, password, kind)
VALUES ('Edgar', 'Porkchops', 'porkboyslim@email.com', 'Password6', 'Business');
INSERT INTO Business_Customer (customer_id, business_name, category, gross_annual_income)
VALUES (6, 'The Basement', 'Entertainment', 70000.00);
INSERT INTO Addresses (street, city, state, zip)
VALUES('1 Main St', 'New York', 'NY', '10025');
UPDATE Customers SET address_id=6 WHERE customer_id=6;

INSERT INTO Stores(store_id, region_id)
VALUES (1, 1);
INSERT INTO Stores(store_id, region_id)
VALUES (2, 2);
INSERT INTO Stores(store_id, region_id)
VALUES (3, 3);
INSERT INTO Stores(store_id, region_id)
VALUES (4, 4);
INSERT INTO Stores(store_id, region_id)
VALUES (5, 5);

INSERT INTO Salespersons (f_name, l_name, email, job_title_id, store_id)
VALUES ('Bob', 'Johnson', 'bjohnson@email.com', 1, 1);
UPDATE Salespersons SET password = 'Password12' WHERE f_name = 'Bob';
INSERT INTO Salespersons (f_name, l_name, email, job_title_id, store_id)
VALUES ('Rob', 'Johnson', 'rjohnson@email.com', 1, 2);
UPDATE Salespersons SET password = 'Password11' WHERE f_name = 'Rob';
INSERT INTO Salespersons (f_name, l_name, email, job_title_id, store_id)
VALUES ('Robert', 'Johnson', 'robertj@email.com', 1, 3);
UPDATE Salespersons SET password = 'Password10' WHERE f_name = 'Robert';
INSERT INTO Salespersons (f_name, l_name, email, job_title_id, store_id)
VALUES ('Robby', 'Johnson', 'robbyj@email.com', 1, 4);
UPDATE Salespersons SET password = 'Password9' WHERE f_name = 'Robby';
INSERT INTO Salespersons (f_name, l_name, email, job_title_id, store_id)
VALUES ('Bobby', 'Johnson', 'bobbyj@email.com', 1, 5);
UPDATE Salespersons SET password = 'Password8' WHERE f_name = 'Bobby';
INSERT INTO Salespersons (f_name, l_name, email, password, job_title_id, store_id)
VALUES ('Vlad', 'Zadorozhny', 'vladzad@email.com', 'Password7', 2, 5);
INSERT INTO Salespersons (f_name, l_name, email, password, job_title_id, store_id)
VALUES ('Hungry', 'Jake', 'hungryjake@email.com', 'Password13', 3, 1);
INSERT INTO Salespersons (f_name, l_name, email, password, job_title_id, store_id)
VALUES ('Garfield', 'Lasagna', 'hungryjake@email.com', 'Password14', 3, 2);
INSERT INTO Salespersons (f_name, l_name, email, password, job_title_id, store_id)
VALUES ('Linda', 'Brumsby', 'lbrumsby@email.com', 'Password15', 1, 5);
INSERT INTO Salespersons (f_name, l_name, email, password, job_title_id, store_id)
VALUES ('Susan', 'Edwards', 'suzzz@email.com', 'Password16', 1, 4);

UPDATE Regions SET manager_id = 1 WHERE region_id = 1;
UPDATE Regions SET manager_id = 3 WHERE region_id = 2;
UPDATE Regions SET manager_id = 4 WHERE region_id = 3;
UPDATE Regions SET manager_id = 5 WHERE region_id = 4;
UPDATE Regions SET manager_id = 6 WHERE region_id = 5;

UPDATE Stores SET manager_id = 1 WHERE store_id = 1;
UPDATE Stores S SET S.salesperson_num = (SELECT COUNT(store_id) FROM Salespersons WHERE store_id=1) WHERE S.store_id=1;
UPDATE Stores SET manager_id = 3 WHERE store_id = 2;
UPDATE Stores S SET S.salesperson_num = (SELECT COUNT(store_id) FROM Salespersons WHERE store_id=2) WHERE S.store_id=2;
UPDATE Stores SET manager_id = 4 WHERE store_id = 3;
UPDATE Stores S SET S.salesperson_num = (SELECT COUNT(store_id) FROM Salespersons WHERE store_id=3) WHERE S.store_id=3;
UPDATE Stores SET manager_id = 5 WHERE store_id = 4;
UPDATE Stores S SET S.salesperson_num = (SELECT COUNT(store_id) FROM Salespersons WHERE store_id=4) WHERE S.store_id=4;
UPDATE Stores SET manager_id = 6 WHERE store_id = 5;
UPDATE Stores S SET S.salesperson_num = (SELECT COUNT(store_id) FROM Salespersons WHERE store_id=5) WHERE S.store_id=5;

INSERT INTO Transactions (customer_id, salesperson_id)
SELECT 1, p.salesperson_id
FROM Salespersons p, Stores s, Regions r, States t, addresses a, customers c
WHERE p.store_id=s.store_id AND s.region_id=r.region_id AND r.region_id=t.region_id AND t.iso=a.state AND a.address_id=c.address_id
AND c.customer_id=1;
INSERT INTO Cart_Items (created_date, quantity, cart_id, product_id)
VALUES (NOW(), 3, 1, 1);
INSERT INTO Cart_Items (created_date, quantity, cart_id, product_id)
VALUES (NOW(), 1, 1, 12);
UPDATE Transactions SET order_date=NOW() WHERE order_num=1;

INSERT INTO Transactions (customer_id, salesperson_id)
SELECT 2, p.salesperson_id
FROM Salespersons p, Stores s, Regions r, States t, addresses a, customers c
WHERE p.store_id=s.store_id AND s.region_id=r.region_id AND r.region_id=t.region_id AND t.iso=a.state AND a.address_id=c.address_id
AND c.customer_id=2;
INSERT INTO Cart_Items (created_date, quantity, cart_id, product_id)
VALUES (NOW(), 2, 2, 9);
INSERT INTO Cart_Items (created_date, quantity, cart_id, product_id)
VALUES (NOW(), 7, 2, 10);
INSERT INTO Cart_Items (created_date, quantity, cart_id, product_id)
VALUES (NOW(), 1, 2, 20);

INSERT INTO Transactions (customer_id, salesperson_id)
SELECT 6, p.salesperson_id
FROM Salespersons p, Stores s, Regions r, States t, addresses a, customers c
WHERE p.store_id=s.store_id AND s.region_id=r.region_id AND r.region_id=t.region_id AND t.iso=a.state AND a.address_id=c.address_id
AND c.customer_id=6;
INSERT INTO Cart_Items (created_date, quantity, cart_id, product_id)
VALUES (NOW(), 1, 3, 14);
UPDATE Transactions SET order_date=NOW() WHERE order_num=3;
INSERT INTO Transactions (customer_id, salesperson_id)
SELECT 6, p.salesperson_id
FROM Salespersons p, Stores s, Regions r, States t, addresses a, customers c
WHERE p.store_id=s.store_id AND s.region_id=r.region_id AND r.region_id=t.region_id AND t.iso=a.state AND a.address_id=c.address_id
AND c.customer_id=6;
INSERT INTO Cart_Items (created_date, quantity, cart_id, product_id)
VALUES (NOW(), 25, 4, 28);
UPDATE Transactions SET order_date=NOW() WHERE order_num=4;
INSERT INTO Transactions (customer_id, salesperson_id)
SELECT 6, p.salesperson_id
FROM Salespersons p, Stores s, Regions r, States t, addresses a, customers c
WHERE p.store_id=s.store_id AND s.region_id=r.region_id AND r.region_id=t.region_id AND t.iso=a.state AND a.address_id=c.address_id
AND c.customer_id=6;
INSERT INTO Cart_Items (created_date, quantity, cart_id, product_id)
VALUES (NOW(), 1, 5, 25);
UPDATE Transactions SET order_date=NOW() WHERE order_num=5;

INSERT INTO Transactions (customer_id, salesperson_id)
SELECT 4, p.salesperson_id
FROM Salespersons p, Stores s, Regions r, States t, addresses a, customers c
WHERE p.store_id=s.store_id AND s.region_id=r.region_id AND r.region_id=t.region_id AND t.iso=a.state AND a.address_id=c.address_id
AND c.customer_id=4;
INSERT INTO Cart_Items (created_date, quantity, cart_id, product_id)
VALUES (NOW(), 15, 6, 2);
UPDATE Transactions SET order_date=NOW() WHERE order_num=6;
INSERT INTO Transactions (customer_id, salesperson_id)
SELECT 4, p.salesperson_id
FROM Salespersons p, Stores s, Regions r, States t, addresses a, customers c
WHERE p.store_id=s.store_id AND s.region_id=r.region_id AND r.region_id=t.region_id AND t.iso=a.state AND a.address_id=c.address_id
AND c.customer_id=4;
INSERT INTO Cart_Items (created_date, quantity, cart_id, product_id)
VALUES (NOW(), 2, 7, 6);
UPDATE Transactions SET order_date=NOW() WHERE order_num=7;

INSERT INTO Transactions (customer_id, salesperson_id)
SELECT 5, p.salesperson_id
FROM Salespersons p, Stores s, Regions r, States t, addresses a, customers c
WHERE p.store_id=s.store_id AND s.region_id=r.region_id AND r.region_id=t.region_id AND t.iso=a.state AND a.address_id=c.address_id
AND c.customer_id=5;
INSERT INTO Cart_Items (created_date, quantity, cart_id, product_id)
VALUES (NOW(), 50, 8, 8);
UPDATE Transactions SET order_date=NOW() WHERE order_num=8;

#What are the aggregate sales and profit of the products?
SELECT P.name AS 'Product Name', SUM(I.quantity) AS 'Sales', I.quantity*P.price AS 'Profit'
   FROM Cart_Items I, Products P
WHERE I.product_id = P.product_id
GROUP BY I.product_id
ORDER BY SUM(I.quantity) DESC;

#What are the top product categories?
SELECT PT.type AS 'Product Type', SUM(I.quantity) AS 'Sales'
  FROM Cart_Items I, Products P, Product_Type PT
 WHERE I.product_id = P.product_id
   AND P.product_type_id = PT.product_type_id
GROUP BY P.product_type_id
ORDER BY SUM(I.quantity) DESC;

#How do the various regions compare by sales volume?
SELECT R.name AS 'Region', COUNT(DISTINCT order_num) AS 'Orders Made', SUM(I.quantity) AS 'Items Sold' 
   FROM Cart_Items I, Transactions T, Regions R, Customers C, Addresses A, States S
  WHERE I.cart_id = T.order_num
	AND T.customer_id = C.customer_id
    AND C.address_id = A.address_id
    AND A.state = S.iso
    AND S.region_id = R.region_id
GROUP BY R.region_id;

#Which businesses are buying given products the most?
SELECT B.business_name AS 'Business Name', P.name AS 'Product', SUM(I.quantity) AS 'Orders'
  FROM Products P, Cart_Items I, Transactions T, Customers C, Business_Customer B
 WHERE P.product_id = I.product_id
   AND I.cart_id = T.order_num
   AND T.customer_id = C.customer_id
   AND C.customer_id = B.customer_id
GROUP BY I.product_id
ORDER BY SUM(I.quantity) DESC
 LIMIT 10;
 
#What are the average prices of the product categories?
SELECT T.type, AVG(P.price)
  FROM Products P, Product_Type T
WHERE P.product_type_id = T.product_type_id
GROUP BY P.product_type_id
ORDER BY AVG(P.price) ASC;