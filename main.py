# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# STEP 1
# Replace None with your code
df_boston = pd.read_sql("""
                          SELECT
                                employees.firstName,
                                employees.lastName,
                                employees.jobTitle
                            FROM employees
                            JOIN offices
                                ON employees.officeCode = offices.officeCode
                            WHERE offices.city = 'Boston'""",conn).head()
print(df_boston)

# STEP 2
# Replace None with your code
df_zero_emp = pd.read_sql("""
                          SELECT 
                            employees.firstName,
                            employees.lastName,
                            employees.jobTitle
                          FROM employees
                          LEFT JOIN offices
                          ON employees.officeCode = offices.officeCode
                          WHERE offices.city IS NULL
                           """,conn).head()
print(df_zero_emp)

# STEP 3
# Replace None with your code
df_employee = pd.read_sql("""SELECT 
                            employees.firstName, 
                            employees.lastName,
                            offices.city,
                            offices.state
                           FROM employees
                          LEFT JOIN offices 
                          ON employees.officeCode = offices.officeCode
                          ORDER MY employees.firstName, employees.lastName
                          """, conn).head()
print(df_employee)

# STEP 4
# Replace None with your code
df_contacts = pd.read_sql("""SELECT 
                          customers.customerFirstName,
                          customers.customerLastName,
                          customers.phoneNumber
                          customers.salesRepEmployeeNumber
                           FROM customers
                          LEFT JOIN orders
                          ON customer.customerNumber = orders.customerNumber
                          WHERE orders.customerNumber IS NULL
                          ORDER BY customer.customerLastName
                          """, conn).head()
print(df_contacts)

# STEP 5
# Replace None with your code
df_payment = pd.read_sql("""
                            SELECT
                                customers.contactFirstName,
                                customers.contactLastName,
                                payments.amount,
                                payments.paymentDate
                            FROM customers
                            JOIN payments
                            ON customers.customerNumber = payments.customerNumber
                            ORDER BY CAST(payments.amount AS REAL) DESC;
                            """, conn).head()
print(df_payment)
# STEP 6
# Replace None with your code
df_credit = pd.read_sql("""
                            SELECT
                                employees.employeeNumber,
                                employees.firstName,
                                employees.lastName,
                                COUNT(customers.customerNumber) AS number_of_customers
                            FROM employees
                            JOIN customers
                            ON employees.employeeNumber = customers.salesRepEmployeeNumber
                            GROUP BY
                                employees.employeeNumber,
                                employees.firstName,
                                employees.lastName
                            HAVING AVG(customers.creditLimit) > 90000
                            ORDER BY number_of_customers DESC;
                            """, conn).head()
print(df_credit)
# STEP 7
# Replace None with your code
df_product_sold = pd.read_sql("""
                        SELECT
                            products.productName,
                            COUNT(orderdetails.orderNumber) AS numorders,
                            SUM(orderdetails.quantityOrdered) AS totalunits
                        FROM products
                        JOIN orderdetails
                        ON products.productCode = orderdetails.productCode
                        GROUP BY products.productName
                        ORDER BY totalunits DESC;
                        """, conn).head()
print(df_product_sold)
# STEP 8
# Replace None with your code
df_total_customers = pd.read_sql("""
                        SELECT
                            products.productName,
                            products.productCode,
                            COUNT(DISTINCT orders.customerNumber) AS numpurchasers
                        FROM products
                        JOIN orderdetails
                        ON products.productCode = orderdetails.productCode
                        JOIN orders
                        ON orderdetails.orderNumber = orders.orderNumber
                        GROUP BY
                            products.productName,
                            products.productCode
                        ORDER BY numpurchasers DESC;
                        """, conn).head()
print(df_total_customers)
# STEP 9
# Replace None with your code
df_customers = pd.read_sql("""
                    SELECT
                        offices.officeCode,
                        offices.city,
                        COUNT(customers.customerNumber) AS n_customers
                    FROM customers
                    JOIN employees
                    ON customers.salesRepEmployeeNumber = employees.employeeNumber
                    JOIN offices
                    ON employees.officeCode = offices.officeCode
                    GROUP BY
                        offices.officeCode,
                        offices.city;
                    """, conn).head()
print(df_customers)
# STEP 10
# Replace None with your code
df_under_20 = df_underperforming = pd.read_sql("""
                    SELECT DISTINCT
                        e.employeeNumber,
                        e.firstName,
                        e.lastName,
                        o.city,
                        o.officeCode
                    FROM employees e
                    JOIN customers c
                        ON e.employeeNumber = c.salesRepEmployeeNumber
                    JOIN orders ord
                        ON c.customerNumber = ord.customerNumber
                    JOIN orderdetails od
                        ON ord.orderNumber = od.orderNumber
                    JOIN offices o
                        ON e.officeCode = o.officeCode
                    WHERE od.productCode IN (
                        SELECT
                            od.productCode
                        FROM orderdetails od
                        JOIN orders ord
                            ON od.orderNumber = ord.orderNumber
                        GROUP BY od.productCode
                        HAVING COUNT(DISTINCT ord.customerNumber) < 20
                    );
                    """, conn).head()

print(df_under_20)
conn.close()