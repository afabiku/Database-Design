-- Drop tables if they exist (in correct order to respect dependencies)
DROP TABLE IF EXISTS employeeCertification, disciplinaryAction, employee, certification, shift, department;

-- Department
CREATE TABLE department (
    DepartmentID SERIAL PRIMARY KEY,
    DepartmentName VARCHAR(100)
);

-- Shift
CREATE TABLE shift (
    ShiftID SERIAL PRIMARY KEY,
    Name VARCHAR(50),
    start_time TIME,
    end_time TIME,
    DaysWorked VARCHAR(100)
);

-- Certification
CREATE TABLE certification (
    CertificationID SERIAL PRIMARY KEY,
    CertificationName VARCHAR(100),
    Description TEXT
);

-- Employee
CREATE TABLE employee (
    EmployeeID SERIAL PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    StartDate DATE,
    Salary NUMERIC(10,2),
    Status VARCHAR(20) CHECK (Status IN ('Full-Time', 'Part-Time')),
    YearsAtCompany INT,
    Strikes INT,
    PTOUsed INT,
    PTORemaining INT,
    HoursWorked NUMERIC(5,2),
    DepartmentID INT REFERENCES department(DepartmentID),
    ShiftID INT REFERENCES shift(ShiftID)
);

-- Disciplinary Action
CREATE TABLE disciplinaryAction (
    ActionID SERIAL PRIMARY KEY,
    EmployeeID INT REFERENCES employee(EmployeeID),
    ActionType VARCHAR(100),
    ActionDate DATE,
    Description TEXT
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
