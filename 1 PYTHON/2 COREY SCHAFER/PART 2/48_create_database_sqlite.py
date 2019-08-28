"""
full pledge databases are my sql or postgre
create a database using sql lite it is for small and medium size applications
where your database is just going to live on desk and testing and prototyping of an application

SQL lite is standard part of library
no need to install anything
its exremely easy to use because your data base is simple file or it can be in memory database is just lives in RAM.


steps for using SQL Lite database
1)no need to install seperately because it is in standard library just import sqlite3
2)second step is need a connection object to represent our database create a variable and assigned to sqlite3 with connect() method
3)in connect method pass a file or store our data or we can make an in-memory database use(':memory:'') but we use filename in our example
4) so use conn=sqlite3.connect(employee.db) got it
5)now run it so sqlite create a db file in our application with naem 47_employee.db
6)create a cursor to execute some SQL commands
--storage classes and data types in documentatio web page are "NULL INTEGER REAL TEXT BLOB""
# to get the results use methods like this fetchone() fetchmany fetchall

fetchone()-it will get the next row and our results and only return that row if there is no more rows available then it returns none
fetchmany()-it takes argument number like 5 it will return that number of rows as a list and
			there are no rows available it returns empty list
fetchall()-it does not take any arguments it will get the remain rows that are left and return those as list and
			 there are no rows available it returns empty list

SQL lite is also work with SQL Alchemy
SQL Alchemy is popular ORM for python that abstracts away lot of differences between databases 
we use SQL Alchemy with SQL lite to get everything prototype out in our application and when u r ready you could just replace that
with a POSTGRES or MYSQL databasewithout change hardly any of the code
"""

import sqlite3
from employee import Employee

con = sqlite3.connect("48_employee.db")
# con = sqlite3.connect(":memory:")						#it starts freshly in the sense freshly inserts the employees scratch
									#in memory database is nice when testing and you dont want to keep deleting database file over and over
c = con.cursor()

# c.execute("""CREATE TABLE workers(
# 			first text,
# 			last text,
# 			pay integer
# 			)""")

# c.execute("INSERT INTO workers VALUES ('Rajesh', 'Singam', 50000)")
# c.execute("INSERT INTO workers VALUES ('Corey', 'Schafer', 80000)")

# c.execute("SELECT * FROM workers where last='Schafer'")
# print(c.fetchone())

def insert_emp(emp):
	with con:
		c.execute("INSERT INTO workers VALUES(:first,:last,:pay)", {"first": emp.first, "last": emp.last, "pay": emp.pay})

def get_emp_by_name(lastname):
	c.execute("SELECT * FROM workers WHERE last=:last", {'last': lastname})  #select statement does not require context manager
	return c.fetchall()

def update_pay(emp,pay):
	with con:
		c.execute("""UPDATE workers SET pay=:pay WHERE first=:first AND last=:last""",
		{"first":emp.first,"last":emp.last,"pay":pay})

def remove_emp(emp):
	with con:
		c.execute("DELETE FROM workers WHERE first=:first AND last=:last",
					{"first":emp.first,"last":emp.last})


emp_1 = Employee("Nitin", "Bevarse", 10000)
emp_2 = Employee("Balayya", "Bevarse", 1500)

# insert_emp(emp_1)
# insert_emp(emp_2)

emps=get_emp_by_name("Bevarse")
update_pay(emp_2,20000)
remove_emp(emp_1)
print(emps)


# remove_emp(emp_2)
# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.pay)

# common way to insert employee records into workers table but this is not recommend cause it leads to sql injection attacck
# c.execute("INSERT INTO workers VALUES("{}","{}",{})".format(self.first, self.last, self.pay)

# second way to insert employee records into workers table
# c.execute("INSERT INTO workers VALUES(?,?,?)", (emp_1.first, emp_1.last, emp_1.pay))

# third this is most efficient way to insert employee records into workers table corey prefered this
# c.execute("INSERT INTO workers VALUES(:first,:last,:pay)", {"first": emp_2.first, "last": emp_2.last, "pay": emp_2.pay})

# query the database for search the employee table k got it for that we execute select statment
# c.execute("SELECT * FROM workers where last=?", ("bevarse",))
# print(c.fetchall())
# c.execute("SELECT * FROM workers where last=:last", {"last": "Boku"})
# print(c.fetchall())


# con.commit()  # commits the current transaction if u dont see something because of this step skip so please make do step this
con.close()  # after commiting changes its good practice to close the connection to the database
