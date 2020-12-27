from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import keyring
import os

ecommerce_app = Flask(__name__)
ecommerce_app.config['MYSQL_HOST'] = 'localhost'
ecommerce_app.config['MYSQL_USER'] = 'admin'
ecommerce_app.config['MYSQL_PASSWORD'] = ''#keyring.get_password('MySql','root')
ecommerce_app.config['MYSQL_DB'] = 'artifact_db'
ecommerce_app.secret_key = 'mY_seCret_KEy'
ecommerce_app.config['CACHE_TYPE'] = "null"

mysql = MySQL(ecommerce_app)

@ecommerce_app.route('/', methods=['GET', 'POST'])
def index():
    session.permanent = False
    if 'loggedin' in session:
        print(session.get('loggedin'))
    else:
        session['cart_cost'] = 0
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT P.product_id, P.name, P.price, D.image_path FROM products P, product_description D WHERE P.product_id=D.product_id ORDER BY RAND() LIMIT 10')
    itemdata = cursor.fetchall()
    cursor.execute('SELECT type FROM product_type')
    product_type = cursor.fetchall()
    print(f"item_data: {itemdata}")
    cursor.close()
    return render_template('index.html', itemdata=itemdata, product_type=product_type)

@ecommerce_app.route('/login/', methods=['GET', 'POST'])
def login():
    message = ''
    table = ''
    log_session = ''
    if request.method == "POST":
        details = request.form
        email = details['email']
        password = details['password']
        print(f"email: {email}")
        print(f"password: {password}")
        try:
            if request.form['login']=='login':
                print('User Login')
                table = 'Customers'
                log_session = 'loggedin'
                email_loc = 4
                cart_query = True
            elif request.form['login']=='employee':
                print('Employee Login')
                table = 'Salespersons'
                log_session = 'emp_loggedin'
                email_loc = 3
                cart_query = False
            cursor = mysql.connection.cursor()
            cursor.execute(f'SELECT * FROM {table} WHERE `email` = %s AND `password` = %s', (email, password))
            acct = cursor.fetchone()
            if acct:
                print(acct)
                session[log_session] = True
                session['id'] = acct[0]
                print(f"id: {session['id']}")
                session['welcome_name'] = acct[1]
                print(f"name: {session['welcome_name']}")
                session['email'] = acct[email_loc]
                print(f"email: {session['email']}")
                session['kind'] = acct[6]
                print(f"kind: {session['kind']}")
                # Redirect to home page
                message = 'Logged in successfully!'
                if cart_query:
                    cursor.execute(f"SELECT CAST(SUM(I.quantity*P.price) AS CHAR) FROM Transactions T, Cart_Items I, Products P WHERE T.order_date IS NULL AND T.customer_id={session['id']} AND T.order_num=I.cart_id AND I.product_id=P.product_id GROUP BY I.cart_id")
                    session['cart_cost'] = cursor.fetchone()[0]
                    print(session['cart_cost'])
                else:
                    cursor.execute(f"SELECT job_title FROM Job_Titles J, Salespersons S WHERE S.salesperson_id={session['id']} AND S.job_title_id=J.title_id")
                    session['job_title'] = cursor.fetchone()[0]
                    print(session['job_title'])
                cursor.close()
            else:
                # Account doesnt exist or username/password incorrect
                message = 'Incorrect username/password!'
                return render_template('login.html', message=message)
        except:
            mysql.connection.rollback()
            mysql.connection.close()
            message = "Error Occurred"

        print(message)
        return redirect(url_for('index'))
    return render_template('login.html', message=message, cart_cost=session['cart_cost'])

@ecommerce_app.route('/logout/')
def logout():
    session.pop('loggedin', None)
    session.pop('emp_loggedin', None)
    session.pop('id', None)
    session.pop('welcome_name', None)
    session.pop('email', None)
    session.pop('cart_cost', None)
    session.pop('kind', None)
    session.pop('job_title', None)
    #return redirect(request.referrer)
    return redirect(url_for('index'))

@ecommerce_app.route('/view_product/', methods=['GET', 'POST'])
def view_product():
    cursor = mysql.connection.cursor()
    prod_id = request.args.get('id')
    if request.method == 'GET':
        name = ''
        inv = ''
        price = ''
        type_id = ''
        type = ''
        desc = ''
        img = ''
        cursor.execute(f"SELECT P.name, P.inventory, P.price, P.product_type_id, T.type, D.product_description, D.image_path FROM Products P, Product_Type T, Product_Description D WHERE P.product_id={prod_id} AND P.product_id=D.product_id AND P.product_type_id=T.product_type_id")
        prod_data = cursor.fetchone()
        if prod_data:
            name = prod_data[0]
            inv = prod_data[1]
            price = prod_data[2]
            type_id = prod_data[3]
            type = prod_data[4]
            desc = prod_data[5]
            img = prod_data[6]
        return render_template('view_product.html', product_id=id, name=name, inv=inv, price=price, type_id=type_id, type=type, desc=desc, img=img)
    elif request.method == 'POST':
        details = request.form
        quant = details['quantity']
        print(f"Product ID: {prod_id}")
        print(f"Quantity: {quant}")
        print(f"Customer ID: {session['id']}")
        try:
            cursor.execute(f"SELECT order_num FROM Transactions WHERE order_date IS NULL AND customer_id={session['id']}")
            order_info = cursor.fetchone()
            print(order_info)
            if order_info:
                order_num = order_info[0]
                print(f"existing cart #{order_num} found")
            else:
                print("attempting new cart creation")
                sql = "INSERT INTO Transactions (customer_id, salesperson_id) "\
                      "SELECT %s, p.salesperson_id "\
                      "FROM Salespersons p, Stores s, Regions r, States t, addresses a, customers c "\
                      "WHERE p.store_id=s.store_id AND s.region_id=r.region_id AND r.region_id=t.region_id "\
                      "AND t.iso=a.state AND a.address_id=c.address_id AND c.customer_id=%s"
                print(sql)
                cursor.execute(sql, (session['id'], session['id']))
                print("cart created")
                mysql.connection.commit()
                cursor.execute(f"SELECT order_num FROM Transactions WHERE order_date IS NULL AND customer_id={session['id']}")
                order_num = cursor.fetchone()[0]
                print(f"new order num: {order_num}")
            cursor.execute(f"INSERT INTO Cart_Items (created_date, quantity, cart_id, product_id) VALUES (NOW(), {quant}, {order_num}, {prod_id})")
            print("insert success")
            cursor.execute(f"SELECT CAST(SUM(I.quantity*P.price) AS CHAR) FROM Transactions T, Cart_Items I, Products P WHERE T.order_date IS NULL AND T.customer_id={session['id']} AND T.order_num={order_num} AND T.order_num=I.cart_id AND I.product_id=P.product_id GROUP BY T.order_num")
            session['cart_cost'] = cursor.fetchone()[0]
            mysql.connection.commit()
        except:
            print("failed to add item")
            mysql.connection.rollback()
        return redirect(url_for("cart"))
    return render_template('view_product.html')

@ecommerce_app.route('/empty_cart/')
def empty_cart():
    cursor = mysql.connection.cursor()
    if session['id']:
        cursor.execute(f"SELECT order_num FROM Transactions WHERE customer_id={session['id']} AND order_date IS NULL")
        order_num = cursor.fetchone()[0]
        cursor.execute(f"DELETE FROM Cart_Items WHERE cart_id={order_num}")
        mysql.connection.commit()
        session.pop('cart_cost', None)
    return redirect(request.referrer)
    #return redirect(url_for('index'))

@ecommerce_app.route('/remove_item/')
def remove_item():
    cursor = mysql.connection.cursor()
    order_num = request.args.get('cart', None)
    product_id = request.args.get('product', None)
    print(f"Order Number: {order_num}")
    print(f"Product ID: {product_id}")
    try:
        cursor.execute(f"DELETE FROM Cart_Items WHERE cart_id={order_num} AND product_id={product_id}")
        print("delete item success")
        cursor.execute(f"SELECT CAST(SUM(I.quantity*P.price) AS CHAR) FROM Transactions T, Cart_Items I, Products P WHERE T.order_date IS NULL AND T.customer_id={session['id']} AND T.order_num={order_num} AND I.product_id=P.product_id GROUP BY I.cart_id")
        session['cart_cost'] = cursor.fetchone()[0]
        mysql.connection.commit()
    except:
        print("delete failed")
        mysql.connection.rollback()
    cursor.close()
    print(f"Cart Cost: ${session['cart_cost']}")
    return redirect(url_for('cart'))

@ecommerce_app.route('/signup/', methods=['GET', 'POST'])
def signup():
    message = ''
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT type name FROM product_type')
    product_type = cursor.fetchall()
    cursor.close()
    if request.method == "POST":
        details = request.form
        firstname = details['firstname']
        lastname = details['lastname']
        emailid =details['emailid']
        phn = details['phonenumber']
        password = details['password']
        confirmpassword = details['confirmpassword']
        # address
        address = details['address']
        state = details['state']
        city = details['city']
        zipcode = details['zipcode']
        #kind of customer
        kind = details['kind']
        age = details['age']
        gender = details['gender']
        annual_income = details['income']
        category = details['category']
        business_name = details['business_name']
        #address id number latest
        cursor = mysql.connection.cursor()
        #cursor.execute('SELECT address_id name FROM addresses')
        #address_id = cursor.fetchall()
        #print(f"address_id: {address_id[-1][0]}")
        #try:
            #address_id = address_id[-1][0]+1
        #except IndexError as e:
            #address_id =1
        # Match Password Check
        if password == confirmpassword:
            # raise ecommerce_app.ValidationError("Passwords must match.")
            print("password matched")
        print(f"firstName: {firstname}")
        print(f"lastName: {lastname}")
        print(f"phone number: {phn}")
        print(f"emailid: {emailid}")
        print(f"password: {password}")
        print(f"confirmpassword: {confirmpassword}")
        print(f"address: {address}")
        print(f"state: {state}")
        print(f"city: {city}")
        print(f"zipcode: {zipcode}")
        print(f'details: {details.items()}')
        print(f'kind: {kind}')
        print(f'age: {age}')
        print(f'gender: {gender}')
        print(f'income: {annual_income}')
        print(f'business_name: {details["business_name"]}')
        try:
            found_empty = False
            for key, value in details.items():
                if value == '':
                    print(f'key: {key}')
                    found_empty = True
                    break
                # Address and customer into the table
                if found_empty==False:
                    cursor.execute(f'INSERT INTO addresses(street,state,city,zip) VALUES'
                                   f'("{address}","{state}","{city}","{zipcode}")')
                    cursor.execute(f'SELECT address_id FROM addresses WHERE street="{address}" AND state="{state}" AND city="{city}" AND zip="{zipcode}"')
                    address_id = cursor.fetchone()[0]
                    print(f"address ID: {address_id}")
                    cursor.execute(f'INSERT INTO Customers(f_name, l_name, email, password, phone, kind, address_id)'
                                   f'VALUES ("{firstname}", "{lastname}","{emailid}","{password}", "{phn}", "{kind}", "{address_id}")')
                    cursor.execute(f'SELECT customer_id FROM Customers WHERE f_name="{firstname}" AND l_name="{lastname}" AND email="{emailid}" AND password="{password}" AND phone="{phn}" AND kind="{kind}" AND address_id={address_id}')
                    customer_id = cursor.fetchone()[0]
                    if(kind=='personal'):
                        print("personal")
                        print(customer_id)
                        cursor.execute(f"INSERT INTO Home_Customer(customer_id, gender, dob, income) "
                                       f"VALUES({customer_id}, '{gender}', str_to_date('{age}', '%Y-%m-%d'), {annual_income})")
                    else:
                        print("business")
                        cursor.execute(f'INSERT INTO business_customer(customer_id,business_name,category,gross_annual_income) '
                                       f'VALUES({customer_id},"{business_name}","{category}",{annual_income})')
                    mysql.connection.commit()
                    print('success')
                cursor.close()
                message = "Sign-up Successfully!"
        except Exception as e:
            mysql.connection.rollback()
            cursor.close()
            message = "Error Occurred"
            print(e)
        #if session['emp_loggedin']:
            #return redirect(url_for('customers'))
        #else:
        return render_template('login.html', product_type=product_type, error=message)
    return render_template('signup.html', product_type=product_type, error=message)

@ecommerce_app.route('/search_result/', methods=['GET', 'POST'])
def search_result():
    cursor = mysql.connection.cursor()
    print(request)
    cursor.execute('SELECT type name FROM product_type')
    product_type = cursor.fetchall()
    if request.method == "POST":
        details = request.form
        print(details)
        if 'searchtext' in details:
            text = details['searchtext']
            global Search_Text
            Search_Text = text
            # cursor.execute(f'SELECT products.name FROM products WHERE products.name LIKE "{text}%" or products.name LIKE '
            #                f'"%{text}" or products.name LIKE "%{text}% "')
            cursor.execute(f'SELECT products.product_id, products.name, products.price, product_description.image_path FROM'
                           f' products,product_description WHERE (products.product_id = product_description.product_id AND'
                           f' products.name LIKE "%{text}") OR (products.product_id = product_description.product_id AND'\
                           f' products.name LIKE "{text}% ") OR (products.product_id = product_description.product_id AND'\
                           f' products.name LIKE "%{text}%")')
            # products_name = cursor.fetchall()

        else:
            print(Search_Text)
            text= Search_Text
            if 'price-ascending' in details['sort_by']:

                cursor.execute(
                    f'SELECT products.product_id, products.name, products.price, product_description.image_path FROM'
                    f' products,product_description WHERE (products.product_id = product_description.product_id AND'
                    f' products.name LIKE "%{text}") OR (products.product_id = product_description.product_id AND' \
                    f' products.name LIKE "{text}% ") OR (products.product_id = product_description.product_id AND' \
                    f' products.name LIKE "%{text}%") order by products.price asc')
            elif 'price-descending' in details['sort_by']:
                cursor.execute(
                    f'SELECT products.product_id, products.name, products.price, product_description.image_path FROM'
                    f' products,product_description WHERE (products.product_id = product_description.product_id AND'
                    f' products.name LIKE "%{text}") OR (products.product_id = product_description.product_id AND' \
                    f' products.name LIKE "{text}% ") OR (products.product_id = product_description.product_id AND' \
                    f' products.name LIKE "%{text}%") order by products.price desc')

        products_name = cursor.fetchall()
        print(f"products_name: {products_name}")
        cursor.close()
    return render_template('search_result.html', itemdata=products_name, product_type=product_type)

@ecommerce_app.route('/page1/', methods=['GET', 'POST'])
def categories():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM product_type')
    product_type = cursor.fetchall()
    get_type_id = request.args.get('product_type_id')
    print(f"{request.args.get('product_type_id')}")
    # cursor.execute(f'SELECT product_id, name, price FROM products WHERE product_type_id = {get_type_id}')
    cursor.execute(f'SELECT products.product_id, products.name, products.price,product_description.image_path FROM products, product_description WHERE products.product_id=product_description.product_id and products.product_type_id = {get_type_id}')
    item_data = cursor.fetchall()
    print(f"item_data: {item_data}")
    # Type of product to display on page
    cursor.execute(f'SELECT type FROM  product_type WHERE product_type.product_type_id = {get_type_id}')
    heading_type = cursor.fetchall()
    # print(f"heading_type: {heading_type}")
    cursor.close()
    return render_template('page1.html', itemdata=item_data, product_type=product_type, heading_type=heading_type)

@ecommerce_app.route('/cart/', methods=['GET', 'POST'])
def cart():
    message = ''
    success = ''
    order_id = ''
    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT T.order_num FROM Transactions T, Cart_Items I, Products P, Product_Description D WHERE T.order_num=I.cart_id AND I.product_id=P.product_id AND P.product_id=D.product_id AND T.customer_id={session['id']} AND order_date IS NULL")
    cart_info = cursor.fetchone()
    if cart_info:
        print("valid cart found")
        order_id = cart_info[0]
    else:
        sql = "INSERT INTO Transactions (customer_id, salesperson_id) " \
              "SELECT %s, p.salesperson_id " \
              "FROM Salespersons p, Stores s, Regions r, States t, addresses a, customers c " \
              "WHERE p.store_id=s.store_id AND s.region_id=r.region_id AND r.region_id=t.region_id " \
              "AND t.iso=a.state AND a.address_id=c.address_id AND c.customer_id=%s"
        cursor.execute(sql, (session['id'], session['id']))
        print("cart created")
        mysql.connection.commit()
        cursor.execute(f"SELECT T.order_num FROM Transactions T, Cart_Items I, Products P, Product_Description D WHERE T.order_num=I.cart_id AND I.product_id=P.product_id AND P.product_id=D.product_id AND T.customer_id={session['id']} AND order_date IS NULL")
        order_info = cursor.fetchone()
        if order_info:
            order_id = order_info[0]
    print(f"Order ID: {order_id}")
    cursor.execute(f"SELECT T.order_num, I.product_id, P.name, D.product_description, D.image_path, I.quantity, P.inventory, P.price, P.price*I.quantity AS \'Cost\', I.created_date FROM Transactions T, Cart_Items I, Products P, Product_Description D WHERE T.order_num=I.cart_id AND I.product_id=P.product_id AND P.product_id=D.product_id AND T.customer_id={session['id']} AND order_date IS NULL ORDER BY I.item_id")
    cart_data = cursor.fetchall()
    if cart_data:
        print(cart_data)
        if request.method == "POST":
            try:
                cursor.execute(f"SELECT P.product_id, P.inventory, I.quantity FROM Products P, Cart_Items I WHERE P.product_id=I.product_id AND I.cart_id={order_id} ORDER BY I.product_id")
                inventory_comp = cursor.fetchall()
                print(inventory_comp)
                inv_check = True
                for row in inventory_comp:
                    inv = row[1]
                    quant = row[2]
                    if quant > inv:
                        inv_check = False
                print(f"Inventory check is {inv_check}")
                money_check = True
                print(f"Customer Type: {session['kind']}")
                if session['kind'] == "Personal":
                    cursor.execute(f"SELECT income FROM Home_Customer H, Customers C WHERE C.customer_id={session['id']} AND H.customer_id=C.customer_id")
                    budget = cursor.fetchone()
                elif session['kind'] == 'Business':
                    cursor.execute(f"SELECT gross_annual_income FROM Business_Customer B, Customers C WHERE C.customer_id={session['id']} AND B.customer_id=C.customer_id")
                    budget = cursor.fetchone()
                print(f"Budget: {budget[0]}")
                print(f"Cart cost: {session['cart_cost']}")
                if float(session['cart_cost']) > float(budget[0]):
                    money_check = False
                print(f"Money check is {money_check}")
                if inv_check and money_check:
                    print('Checks passed')
                    cursor.execute(f"UPDATE Transactions SET order_date = NOW() WHERE order_num={order_id}")
                    for row in cart_data:
                        print(row)
                        cursor.execute(f"UPDATE Products SET inventory=inventory-{row[5]} WHERE  product_id={row[0]}")
                    if session['kind'] == 'Personal':
                        cursor.execute(f"UPDATE Home_Customer SET income = income-{session['cart_cost']} WHERE customer_id={session['id']}")
                    elif session['kind'] == 'Business':
                        cursor.execute(f"UPDATE Business_Customer SET gross_annual_income = gross_annual_income-{session['cart_cost']} WHERE customer_id={session['id']}")
                    message = 'Transaction Complete - Order Processed!'
                    session.pop('cart_cost', None)
                    success = True
                    mysql.connection.commit()
                else:
                    message = 'Error: Unable to complete transaction'
                    success = False
                    return render_template('cart.html', cart_data=cart_data, message=message, success=success)
                cursor.close()
            except:
                mysql.connection.rollback()
                mysql.connection.close()
                success = False
                message = "Error Occurred"
    else:
        message = 'Error Loading Cart'
        success = False
        return render_template('cart.html', cart_data=cart_data, message=message, success=success)
    print(message)
    return render_template('cart.html', cart_data=cart_data, message=message, success=success)

@ecommerce_app.route('/analytics/')
def analytics():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT P.name AS \'Product Name\', SUM(I.quantity) AS \'Sales\', I.quantity*P.price AS \'Profit\' FROM Cart_Items I, Products P WHERE I.product_id = P.product_id GROUP BY I.product_id ORDER BY SUM(I.quantity) DESC')
    product_sales = cursor.fetchall()
    print(product_sales)
    cursor.execute('SELECT PT.type AS \'Product Type\', SUM(I.quantity) AS \'Sales\' FROM Cart_Items I, Products P, Product_Type PT WHERE I.product_id = P.product_id AND P.product_type_id = PT.product_type_id GROUP BY P.product_type_id ORDER BY SUM(I.quantity) DESC')
    product_categories = cursor.fetchall()
    print(product_categories)
    cursor.execute('SELECT R.name AS \'Region\', COUNT(DISTINCT order_num) AS \'Orders Made\', SUM(I.quantity) AS \'Items Sold\' FROM Cart_Items I, Transactions T, Regions R, Customers C, Addresses A, States S WHERE I.cart_id = T.order_num AND T.customer_id = C.customer_id AND C.address_id = A.address_id AND A.state = S.iso AND S.region_id = R.region_id GROUP BY R.region_id')
    region_sales = cursor.fetchall()
    print(region_sales)
    cursor.execute('SELECT B.business_name AS \'Business Name\', P.name AS \'Product\', SUM(I.quantity) AS \'Orders\' FROM Products P, Cart_Items I, Transactions T, Customers C, Business_Customer B WHERE P.product_id = I.product_id AND I.cart_id=T.order_num AND T.customer_id = C.customer_id AND C.customer_id = B.customer_id GROUP BY I.product_id ORDER BY SUM(I.quantity) DESC LIMIT 10')
    business_purchases = cursor.fetchall()
    print(business_purchases)
    cursor.execute('SELECT T.type, AVG(P.price) FROM Products P, Product_Type T WHERE P.product_type_id = T.product_type_id GROUP BY P.product_type_id ORDER BY AVG(P.price) ASC')
    type_price = cursor.fetchall()
    print(type_price)
    cursor.close()
    return render_template('analytics.html', product_sales=product_sales, product_categories=product_categories, region_sales=region_sales, business_purchases=business_purchases, type_price=type_price)

@ecommerce_app.route('/orders/')
def orders():
    cursor = mysql.connection.cursor()
    order_data = ''
    if session['id']:
        sql = "SELECT T.order_num, T.order_date, P.name, I.quantity, I.quantity*P.price, S.f_name, S.l_name "\
              "FROM Transactions T, Cart_Items I, Products P, Salespersons S "\
              "WHERE T.customer_id=%s "\
              "AND T.order_num=I.cart_id "\
              "AND I.product_id=P.product_id "\
              "AND T.salesperson_id=S.salesperson_id "\
              "GROUP BY T.order_num, I.item_id"
        print(sql)
        cursor.execute(sql, (session['id'],))
        order_data = cursor.fetchall()
        print(order_data)
    cursor.close()
    return render_template('orders.html', order_data=order_data)

@ecommerce_app.route('/customers/')
def customers():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT C.customer_id, C.f_name, C.l_name, C.phone, C.email, C.kind, A.street, A.city, A.zip, A.state FROM Customers C, Addresses A WHERE C.address_id = A.address_id ORDER BY C.customer_id ASC')
    cust_data = cursor.fetchall()
    print(cust_data)
    return render_template('customers.html', cust_data=cust_data)

@ecommerce_app.route('/edit_customer/', methods=['GET', 'POST'])
def edit_customer():
    message = ''
    cursor = mysql.connection.cursor()
    edit_id = request.args.get('id', None)
    if request.method == "GET":
        print(f"Edited User's ID: {edit_id}")
        edit_kind = request.args.get('kind', None)
        if edit_kind == 'Personal':
            cursor.execute(f"SELECT C.f_name, C.l_name, C.phone, C.email, A.street, A.city, A.zip, A.state, H.gender, H.dob, H.income FROM Customers C, Home_Customer H, Addresses A WHERE C.customer_id={edit_id} AND C.customer_id=H.customer_id AND C.address_id=A.address_id")
            cust_data = cursor.fetchone()
        elif edit_kind == 'Business':
            cursor.execute(f"SELECT C.f_name, C.l_name, C.phone, C.email, A.street, A.city, A.zip, A.state, B.business_name, B.category, B.gross_annual_income FROM Customers C, Business_Customer B, Addresses A WHERE C.customer_id={edit_id} AND C.customer_id=B.customer_id AND C.address_id=A.address_id")
            cust_data = cursor.fetchone()
        if cust_data:
            fname = cust_data[0]
            lname = cust_data[1]
            phone = cust_data[2]
            email = cust_data[3]
            street = cust_data[4]
            city = cust_data[5]
            zip = cust_data[6]
            state = cust_data[7]
            income = cust_data[10]
            #gender = ''
            #age = ''
            #bus_name = ''
            #category = ''
            #if edit_kind == 'Personal':
            #    gender = cust_data[8]
            #    age = cust_data[9]
            #elif edit_kind == 'Business':
            #    bus_name = cust_data[8]
            #    category = cust_data[9]
        #print(state)
        print(edit_kind)
        return render_template('edit_customer.html', firstname=fname, lastname=lname, emailid=email, phonenumber=phone, address=street, city=city, zipcode=zip, state=state, kind=edit_kind,income=income)#, gender=gender, age=age, business_name=bus_name, category=category)
    elif request.method == "POST":
        details = request.form
        firstname = details['firstname']
        lastname = details['lastname']
        emailid = details['emailid']
        phn = details['phonenumber']
        # address
        address = details['address']
        state = details['state']
        city = details['city']
        zipcode = details['zipcode']
        # kind of customer
        kind = details['kind']
        #if kind == 'Personal':
        #    age = details['age']
        #    gender = details['sex']
        #    print(f'age: {age}')
        #    print(f'gender: {gender}')
        #elif kind == 'Business':
        #    business_name = details['business_name']
        #    category = details['category']
        #    print(f'business_name: {details["business_name"]}')
        #    print(f'business_category: {details["category"]}')
        annual_income = details['income']
        cursor.execute(f"SELECT A.address_id FROM Addresses A, Customers C WHERE C.customer_id={edit_id} AND C.address_id=A.address_id")
        address_id = cursor.fetchone()[0]
        print(f"firstName: {firstname}")
        print(f"lastName: {lastname}")
        print(f"emailid: {emailid}")
        print(f"phone: {phn}")
        print(f"address_id: {address_id}")
        print(f"address: {address}")
        print(f"state: {state}")
        print(f"city: {city}")
        print(f"zipcode: {zipcode}")
        print(f'customer type: {kind}')
        print(f'income: {details["income"]}')
        try:
            cursor.execute(f"UPDATE Addresses SET street='{address}',state='{state}', city='{city}', zip='{zipcode}' WHERE address_id={address_id}")
            print("address update success")
            cursor.execute(f"UPDATE Customers SET f_name='{firstname}', l_name='{lastname}', email='{emailid}', phone='{phn}', kind='{kind}' WHERE customer_id={edit_id}")
            print("customer update success")
            #if kind == 'Personal':
            #    cursor.execute(f"UPDATE Home_Customer SET gender='{gender}', dob='{age}', income={annual_income} WHERE customer_id={edit_id}")
            #    print("personal")
            #else:
            #    cursor.execute(f"UPDATE Business_Customer SET business_name='{business_name}', category='{category}', gross_annual_income={annual_income} WHERE customer_id={edit_id}")
            #    print("business")
            mysql.connection.commit()
            print('success')
            cursor.close()
            message = "Edited Successfully!"
        except Exception as e:
            mysql.connection.rollback()
            cursor.close()
            message = "Error Occurred"
            print(message)
        return redirect(url_for('customers'))
    return render_template('edit_customer.html', message=message)

@ecommerce_app.route('/remove_customer/')
def remove_customer():
    cursor = mysql.connection.cursor()
    cust_id = request.args.get('id', None)
    print(cust_id)
    try:
        cursor.execute(f"DELETE FROM Customers WHERE customer_id={cust_id}")
        mysql.connection.commit()
        print("delete customer success")
    except:
        mysql.connection.rollback()
        print("delete customer failure")
    cursor.close()
    return redirect(url_for('customers'))

@ecommerce_app.route('/products/')
def products():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT P.product_id, P.name, P.inventory, P.price, T.type, D.product_description, D.image_path FROM Products P, Product_Type T, Product_Description D WHERE P.product_id = D.product_id AND P.product_type_id = T.product_type_id ORDER BY P.product_id ASC')
    prod_data = cursor.fetchall()
    print(prod_data)
    return render_template('products.html', prod_data=prod_data)

@ecommerce_app.route('/edit_product/', methods=['GET', 'POST'])
def edit_product():
    message = ''
    cursor = mysql.connection.cursor()
    edit_id = request.args.get('id', None)
    new = request.args.get('new', None)
    print(f"Edited Product's ID: {edit_id}")
    print(f"Is new product: {new}")
    if request.method == "GET":
        name = ''
        inv = ''
        price = ''
        type_id = ''
        type = ''
        desc = ''
        img = ''
        if new == 'False':
            cursor.execute(f"SELECT P.name, P.inventory, P.price, P.product_type_id, T.type, D.product_description, D.image_path FROM Products P, Product_Type T, Product_Description D WHERE P.product_id={edit_id} AND P.product_id=D.product_id AND P.product_type_id=T.product_type_id")
            prod_data = cursor.fetchone()
            if prod_data:
                name = prod_data[0]
                inv = prod_data[1]
                price = prod_data[2]
                type_id = prod_data[3]
                type = prod_data[4]
                desc = prod_data[5]
                img = prod_data[6]
        cursor.execute("SELECT * FROM Product_Type")
        type_data = cursor.fetchall()
        return render_template('edit_product.html', product_id=edit_id, name=name, inv=inv, price=price, type_id=type_id, type=type, desc=desc, img=img, type_data=type_data)
    elif request.method == "POST":
        details = request.form
        name = details['name']
        inv = details['inv']
        price = details['price']
        type_id = details['type']
        desc = details['desc']
        img = details['img']
        print(f"Name: {name}")
        print(f"Inventory: {inv}")
        print(f"Price: {price}")
        print(f"Type ID: {type_id}")
        print(f"Description: {desc}")
        print(f"Image Path: {img}")
        try:
            if new == 'False':
                cursor.execute(f"UPDATE Products SET name='{name}', inventory={inv}, price={price}, product_type_id={type_id} WHERE product_id={edit_id}")
                print("product update success")
                cursor.execute(f"UPDATE Product_Description SET product_description='{desc}', image_path='{img}' WHERE product_id={edit_id}")
                print("description update success")
            else:
                cursor.execute(f"INSERT INTO Products (name, inventory, price, product_type_id) VALUES ('{name}', {inv}, {price}, {type_id})")
                print("product insert success")
                cursor.execute(f"SELECT product_id FROM Products WHERE name='{name}' AND inventory={inv} AND price={price} AND product_type_id={type_id}")
                prod_id = cursor.fetchone()[0]
                cursor.execute(f"INSERT INTO Product_Description (product_id, product_description, image_path) VALUES ({prod_id}, '{desc}', '{img}')")
                print("description insert success")
            mysql.connection.commit()
            print('success')
            cursor.close()
            message = "Edited Successfully!"
        except Exception as e:
            mysql.connection.rollback()
            cursor.close()
            message = "Error Occurred"
            print(message)
        return redirect(url_for('products'))
    return render_template('edit_product.html', message=message)

@ecommerce_app.route('/remove_product/')
def remove_product():
    cursor = mysql.connection.cursor()
    prod_id = request.args.get('id', None)
    print(prod_id)
    try:
        cursor.execute(f"DELETE FROM Products WHERE product_id={prod_id}")
        mysql.connection.commit()
        print("delete product success")
    except:
        mysql.connection.rollback()
        print("delete product failure")
    cursor.close()
    return redirect(url_for('products'))

@ecommerce_app.route('/stores/')
def stores():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT S.store_id, S.salesperson_num, M.f_name, M.l_name, R.name FROM Stores S, Salespersons M, Regions R WHERE S.manager_id = M.salesperson_id AND S.region_id = R.region_id ORDER BY S.store_id ASC')
    store_data = cursor.fetchall()
    print(store_data)
    return render_template('stores.html', store_data=store_data)

@ecommerce_app.route('/edit_store/', methods=['GET', 'POST'])
def edit_store():
    message = ''
    cursor = mysql.connection.cursor()
    edit_id = request.args.get('id', None)
    new = request.args.get('new', None)
    print(f"Edited ID: {edit_id}")
    print(f"Is new store: {new}")
    if request.method == "GET":
        store_data = ''
        manager_id = ''
        manager_firstname = ''
        manager_lastname = ''
        region = ''
        region_name = ''
        if new == 'False':
            cursor.execute(f"SELECT S.manager_id, M.f_name, M.l_name, R.region_id, R.name FROM Stores S, Salespersons M, Regions R WHERE S.store_id={edit_id} AND S.manager_id=M.salesperson_id AND S.region_id=R.region_id")
            store_data = cursor.fetchone()
            if store_data:
                print(store_data)
                manager_id = store_data[0]
                manager_firstname = store_data[1]
                manager_lastname = store_data[2]
                region = store_data[3]
                region_name = store_data[4]
        cursor.execute('SELECT salesperson_id, f_name, l_name FROM Salespersons WHERE job_title_id=1')
        manager_data = cursor.fetchall()
        cursor.execute('SELECT region_id, name FROM Regions')
        region_data = cursor.fetchall()
        return render_template('edit_store.html', store_id=edit_id, manager_id=manager_id, fname=manager_firstname, lname=manager_lastname, region=region, region_name=region_name, manager_data=manager_data, region_data=region_data)
    elif request.method == "POST":
        details = request.form
        manager_id = details['manager_id']
        region_id = details['region_id']
        print(f"Manager ID: {manager_id}")
        print(f"Region ID: {region_id}")
        try:
            if new == 'False':
                cursor.execute(f"UPDATE Stores SET manager_id={manager_id}, region_id={region_id} WHERE store_id={edit_id}")
                print("store update success")
            else:
                cursor.execute(f"INSERT INTO Stores (manager_id, region_id) VALUES ({manager_id}, {region_id})")
                print("store insert success")
                cursor.execute(f"SELECT store_id FROM Stores WHERE manager_id={manager_id} AND region_id={region_id}")
                edit_id = cursor.fetchone()[0]
            cursor.execute(f"UPDATE Salespersons SET store_id={edit_id} WHERE salesperson_id={manager_id}")
            print("manager update success")
            cursor.execute(f"UPDATE Stores S SET S.salesperson_num = (SELECT COUNT(store_id) FROM Salespersons WHERE store_id={edit_id}) WHERE S.store_id={edit_id}")
            print("salesperson count success")
            mysql.connection.commit()
            print('success')
            cursor.close()
            message = "Edited Successfully!"
        except Exception as e:
            mysql.connection.rollback()
            cursor.close()
            message = "Error Occurred"
            print(message)
        return redirect(url_for('stores'))
    return render_template('edit_store.html', message=message)

@ecommerce_app.route('/remove_store/')
def remove_store():
    cursor = mysql.connection.cursor()
    store_id = request.args.get('id', None)
    print(store_id)
    try:
        cursor.execute(f"DELETE FROM Stores WHERE store_id={store_id}")
        mysql.connection.commit()
        print("delete store success")
    except:
        mysql.connection.rollback()
        print("delete store failure")
    cursor.close()
    return redirect(url_for('stores'))

if __name__ == '__main__':
    ecommerce_app.run(debug=True)
    #ecommerce_app.run(debug=False, host='0.0.0.0', port=8000)
