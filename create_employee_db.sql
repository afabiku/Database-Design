-- Drop tables if they exist
DROP TABLE IF EXISTS employeeCertification, disciplinaryAction, employee, certification, shift, department;

-- Department
CREATE TABLE department (
    DepartmentID INT PRIMARY KEY AUTO_INCREMENT,
    DepartmentName VARCHAR(100)
);

-- Shift
CREATE TABLE shift (
    ShiftID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50),
    start_time TIME,
    end_time TIME,
    DaysWorked VARCHAR(100)
);

-- Certification
CREATE TABLE certification (
    CertificationID INT PRIMARY KEY AUTO_INCREMENT,
    CertificationName VARCHAR(100),
    Description TEXT
);

-- Employee
CREATE TABLE employee (
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    StartDate DATE,
    Salary DECIMAL(10,2),
    Status ENUM('Full-Time', 'Part-Time'),
    YearsAtCompany INT,
    Strikes INT,
    PTOUsed INT,
    PTORemaining INT,
    HoursWorked DECIMAL(5,2),
    DepartmentID INT,
    ShiftID INT,
    FOREIGN KEY (DepartmentID) REFERENCES department(DepartmentID),
    FOREIGN KEY (ShiftID) REFERENCES shift(ShiftID)
);

-- Disciplinary Action
CREATE TABLE disciplinaryAction (
    ActionID INT PRIMARY KEY AUTO_INCREMENT,
    EmployeeID INT,
    ActionType VARCHAR(100),
    ActionDate DATE,
    Description TEXT,
    FOREIGN KEY (EmployeeID) REFERENCES employee(EmployeeID)
);

-- Employee Certifications
CREATE TABLE employeeCertification (
    EmployeeID INT,
    CertificationID INT,
    DateObtained DATE,
    PRIMARY KEY (EmployeeID, CertificationID),
    FOREIGN KEY (EmployeeID) REFERENCES employee(EmployeeID),
    FOREIGN KEY (CertificationID) REFERENCES certification(CertificationID)
);
