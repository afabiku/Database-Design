from app import db

class Employee(db.Model):
    __tablename__ = "employee"

    EmployeeID = db.Column("employeeid", db.Integer, primary_key=True)
    FirstName = db.Column("firstname", db.String(50))
    LastName = db.Column("lastname", db.String(50))
    StartDate = db.Column("startdate", db.Date)
    Salary = db.Column("salary", db.Numeric(10, 2))
    Status = db.Column("status", db.String(20))
    YearsAtCompany = db.Column("yearsatcompany", db.Integer)
    Strikes = db.Column("strikes", db.Integer)
    PTOUsed = db.Column("ptoused", db.Integer)
    PTORemaining = db.Column("ptoremaining", db.Integer)
    HoursWorked = db.Column("hoursworked", db.Numeric(5, 2))
    DepartmentID = db.Column("departmentid", db.Integer)
    ShiftID = db.Column("shiftid", db.Integer)
