# MySQL Comprehensive Guide

## Table of Contents
1. [Introduction to MySQL](#introduction-to-mysql)
2. [Database Design and Constraints](#database-design-and-constraints)
3. [Basic SQL Queries](#basic-sql-queries)
4. [Advanced SQL Queries](#advanced-sql-queries)
5. [Subqueries and CTEs](#subqueries-and-ctes)
6. [Joins and Set Operations](#joins-and-set-operations)
7. [ER Diagrams and Normalization](#er-diagrams-and-normalization)
8. [Stored Procedures, Functions, and Triggers](#stored-procedures-functions-and-triggers)
9. [Conclusion](#conclusion)

---

## 1. Introduction to MySQL

### What is MySQL?
MySQL is an open-source relational database management system (RDBMS) that uses SQL (Structured Query Language) for managing and manipulating databases.

### Installation
- **Windows**: Download from [MySQL Official Website](https://dev.mysql.com/downloads/installer/) and follow the installation wizard.
- **Linux**: Use package manager, e.g., `sudo apt-get install mysql-server`.
- **macOS**: Use Homebrew, e.g., `brew install mysql`.

### Basic Setup
```sql
CREATE DATABASE mydatabase;
USE mydatabase;
```

---

## 2. Database Design and Constraints

### Primary Key
```sql
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(100),
    Position VARCHAR(100)
);
```

### Foreign Key
```sql
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    EmployeeID INT,
    OrderDate DATE,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);
```

### Unique Constraint
```sql
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100) UNIQUE
);
```

### Default and NOT NULL
```sql
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) DEFAULT 'noemail@example.com'
);
```

### Composite Primary Key
```sql
CREATE TABLE EmployeeProjects (
    EmployeeID INT,
    ProjectID INT,
    PRIMARY KEY (EmployeeID, ProjectID)
);
```

---

## 3. Basic SQL Queries

### SELECT Statement
```sql
SELECT * FROM Employees;
```

### Arithmetic Operators
```sql
SELECT Salary * 1.1 AS IncreasedSalary FROM Employees;
```

### Comparison and Logical Operators
```sql
SELECT * FROM Employees WHERE Salary > 50000 AND Department = 'Sales';
```

### DISTINCT, ORDER BY, LIMIT, OFFSET
```sql
SELECT DISTINCT Department FROM Employees ORDER BY Department LIMIT 5 OFFSET 2;
```

### IN, NOT IN, LIKE, AS
```sql
SELECT * FROM Employees WHERE Department IN ('Sales', 'Marketing') AND Name LIKE 'J%';
```

---

## 4. Advanced SQL Queries

### Functions
```sql
SELECT UPPER(Name) FROM Employees;
```

### Group Functions and GROUP BY
```sql
SELECT Department, AVG(Salary) FROM Employees GROUP BY Department HAVING AVG(Salary) > 50000;
```

### ALTER TABLE
```sql
ALTER TABLE Employees ADD COLUMN Email VARCHAR(100);
```

---

## 5. Subqueries and CTEs

### Subquery
```sql
SELECT Name FROM Employees WHERE Salary = (SELECT MAX(Salary) FROM Employees WHERE Department = 'Sales');
```

### CTE
```sql
WITH SalesEmployees AS (
    SELECT * FROM Employees WHERE Department = 'Sales'
)
SELECT Name FROM SalesEmployees WHERE Salary > 50000;
```

---

## 6. Joins and Set Operations

### INNER JOIN
```sql
SELECT Employees.Name, Orders.OrderDate FROM Employees INNER JOIN Orders ON Employees.EmployeeID = Orders.EmployeeID;
```

### LEFT JOIN
```sql
SELECT Employees.Name, Orders.OrderDate FROM Employees LEFT JOIN Orders ON Employees.EmployeeID = Orders.EmployeeID;
```

### UNION
```sql
SELECT Name FROM Employees UNION SELECT Name FROM Customers;
```

---

## 7. ER Diagrams and Normalization

### ER Diagram
- **Entities**: Customer, Order, Product
- **Relationships**: Customer places Order, Order contains Product

### Normalization
- **1NF**: Atomic values
- **2NF**: No partial dependencies
- **3NF**: No transitive dependencies

---

## 8. Stored Procedures, Functions, and Triggers

### Stored Procedure
```sql
CREATE PROCEDURE GetEmployeeNames()
BEGIN
    SELECT Name FROM Employees;
END;
```

### Function
```sql
CREATE FUNCTION GetEmployeeCount() RETURNS INT
BEGIN
    RETURN (SELECT COUNT(*) FROM Employees);
END;
```

### Trigger
```sql
CREATE TRIGGER UpdateLog BEFORE UPDATE ON Employees
FOR EACH ROW
BEGIN
    INSERT INTO EmployeeLog VALUES (OLD.EmployeeID, OLD.Name);
END;
```

---

## Conclusion

This guide provides a comprehensive overview of MySQL, from basic setup to advanced topics like stored procedures and triggers. Practice the examples and explore further to deepen your understanding of database management.

Happy coding!