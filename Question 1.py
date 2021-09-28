import sqlite3
conn1 = sqlite3.connect('employee.db')
cursor1 = conn1.cursor()
cursor1.execute("DROP TABLE IF EXISTS EMPLOYEE")
query1 = """CREATE TABLE EMPLOYEE(
        Employee_Id INT PRIMARY KEY,
        Employee_Name CHAR(20), 
        Department_ID INT,
        Salary INT)"""
cursor1.execute(query1)
newcol = "ALTER TABLE EMPLOYEE ADD COLUMN City VARCHAR"
cursor1.execute(newcol)
conn1.execute("INSERT  INTO EMPLOYEE (Employee_Id,Employee_Name,Department_ID,Salary,City)" 
                 "VALUES (1,'Eric',101,10000,'London')")
conn1.execute("INSERT  INTO EMPLOYEE (Employee_Id,Employee_Name,Department_ID,Salary,City)" 
                 "VALUES (2,'Adam',102,20000,'Paris')")
conn1.execute("INSERT  INTO EMPLOYEE (Employee_Id,Employee_Name,Department_ID,Salary,City)" 
                 "VALUES (3,'Otis',103,30000,'Manchester')")
conn1.execute("INSERT  INTO EMPLOYEE (Employee_Id,Employee_Name,Department_ID,Salary,City)" 
                 "VALUES (4,'Ola',104,40000,'Liverpool')")
conn1.execute("INSERT  INTO EMPLOYEE (Employee_Id,Employee_Name,Department_ID,Salary,City)" 
                 "VALUES (5,'Jean',105,50000,'Melbourn')")
cursor1 = conn1.execute("SELECT Employee_Name,Employee_Id,Salary from EMPLOYEE")
print(cursor1.fetchall())
d = input("Enter the first letter of employee")
print(conn1.execute("SELECT * from EMPLOYEE where upper(Employee_Name) LIKE'"+ d +"%'").fetchall())
e = input("Enter the Employee ID")
print(conn1.execute("SELECT * from EMPLOYEE where (Employee_Id) LIKE'"+ e +"%'").fetchall())

a=input("Enter the employee id who you wish to change the name ")
s=input("Enter new employee name")
conn1.execute("UPDATE EMPLOYEE SET Employee_Name = '"+ s +"'where Employee_Id='"+ a +"'")
print(conn1.execute("SELECT * from EMPLOYEE").fetchall())
conn1.commit()
conn1.close()
