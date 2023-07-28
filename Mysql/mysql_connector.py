import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',password='Dreamlife@48#')
# print(mydb)

# To create database :
my_cursor = mydb.cursor()
# my_cursor.execute('create database Mydb_python') # here its being commented because if it runs again it will show error because its already exist.

# # TO show database :
# my_cursor.execute('show databases')
# # for x in my_cursor:
# #     print(x)

# To create table :
my_cursor.execute('use Mydb_python')
# # my_cursor.execute('create table employee(name varchar(250),dept varchar(200),salary int);')
# my_cursor.execute('show tables')
# for x in my_cursor:
#     print(x)

# # inserting values into table :
# sql = "insert into employee values('swetha','python','40000')"
# my_cursor.execute(sql)
# mydb.commit()
# print(my_cursor.rowcount,"record inserted")

# # inserting multiple values into table :
# sql = "insert into employee(name,dept,salary) values(%s,%s,%s)"
# val = [
#     ('niki','MSC',40000),
#     ('sarangi','python',40000),
#     ('sreehari','site eng',15000)
# ]
# my_cursor.executemany(sql,val)
# mydb.commit()
# print(my_cursor.rowcount,"record inserted")

# # To show particular table :
# my_cursor.execute("select * from employee")
# my_result = my_cursor.fetchall()
# for x in my_result:
#     print(x)

# # fetchone() :
# my_cursor.execute("select * from employee")
# my_result = my_cursor.fetchone()
# print(my_result)

# # fetch specific one :
# my_cursor.execute("select * from employee where name = 'swetha'")
# my_result = my_cursor.fetchone()
# print(my_result)

# # To delete a row from table :
# sql = "delete from employee where name = 'sarangi'"
# my_cursor.execute(sql)
# mydb.commit()
# print(my_cursor.rowcount,"record deleted")

# # Update :
# sql = "update employee set dept ='government job' where dept ='MSC'"
# my_cursor.execute(sql)
# mydb.commit()


# # Order by :
# # Order by desc :
# sql = "select * from employee order by name desc"
# my_cursor.execute(sql)
# my_result = my_cursor.fetchall()
# for x in my_result:
#     print(x)

# # Sort the result alphabetically by name :
# sql = "select * from employee order by name"
# my_cursor.execute(sql)
# my_result = my_cursor.fetchall()
# for x in my_result:
#     print(x)
"""
relationship queries :
1. one to one
   eg : user ----> password
2. one to many
   eg : class ----> student
3. many to one
   eg : student ----> course
4. many to many  
   eg : student ----> class        """

# To create another table :
my_cursor.execute('use Mydb_python')
# # my_cursor.execute('create table test(name varchar(250),dept varchar(200),salary int);')
# my_cursor.execute('show tables')
# for x in my_cursor:
#     print(x)

# # inserting values into table :
# sql = "insert into test(name,dept,salary) values(%s,%s,%s)"
# val =[
#     ('ayu','masters in CS',100000),
#     ('shrishti','MBA',75000),
#     ('sanju','IT classes',40000)
# ]
# my_cursor.executemany(sql,val)
# mydb.commit()
# print(my_cursor.rowcount,": values are inserted")
