
### Basic Setup
```sql
CREATE DATABASE mydatabase;
USE mydatabase;
```

---

##  Database Design and Constraints

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

##  Basic SQL Queries

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
SELECT * FROM Employees
WHERE Salary > 50000 AND Department = 'Sales';
```

### DISTINCT, ORDER BY, LIMIT, OFFSET
```sql
SELECT DISTINCT Department
FROM Employees
ORDER BY Department
LIMIT 5
OFFSET 2;
```

### IN, NOT IN, LIKE, AS
```sql
SELECT *
FROM Employees
WHERE Department IN ('Sales', 'Marketing') AND Name LIKE 'J%';
```

---

## Advanced SQL Queries

### Functions
```sql
SELECT UPPER(Name) FROM Employees;
```

### Group Functions and GROUP BY
```sql
SELECT Department, AVG(Salary)
FROM Employees
GROUP BY Department
HAVING AVG(Salary) > 50000;
```

### ALTER TABLE
```sql
ALTER TABLE Employees ADD COLUMN Email VARCHAR(100);
```

---

## Subqueries and CTEs

### Subquery
```sql
SELECT Name
FROM Employees
WHERE Salary = (SELECT MAX(Salary)FROM Employees WHERE Department = 'Sales');
```

### CTE
```sql
WITH SalesEmployees AS (
    SELECT * FROM Employees WHERE Department = 'Sales'
)
SELECT Name FROM SalesEmployees WHERE Salary > 50000;
```

---

##  Joins and Set Operations

### INNER JOIN
```sql
SELECT Employees.Name, Orders.OrderDate
FROM Employees
INNER JOIN Orders ON Employees.EmployeeID = Orders.EmployeeID;
```

### LEFT JOIN
```sql
SELECT Employees.Name, Orders.OrderDate
FROM Employees
LEFT JOIN Orders ON Employees.EmployeeID = Orders.EmployeeID;
```

### UNION
```sql
SELECT Name
FROM Employees
UNION SELECT Name FROM Customers;
```
##  Stored Procedures, Functions, and Triggers

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
