from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class Department(db.Model):
    DepartmentID = db.Column(db.Integer, primary_key=True)
    DepartmentName = db.Column(db.String(100), nullable=False)

class Shift(db.Model):
    ShiftID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50), nullable=False)
    start_time = db.Column(db.String(8))
    end_time = db.Column(db.String(8))
    DaysWorked = db.Column(db.String(100))

class Certification(db.Model):
    CertificationID = db.Column(db.Integer, primary_key=True)
    CertificationName = db.Column(db.String(100))
    Description = db.Column(db.Text)

class Employee(db.Model):
    EmployeeID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50))
    LastName = db.Column(db.String(50))
    StartDate = db.Column(db.Date)
    Salary = db.Column(db.Float)
    Status = db.Column(db.String(20))  # changed from Enum
    YearsAtCompany = db.Column(db.Integer)
    Strikes = db.Column(db.Integer)
    PTOUsed = db.Column(db.Integer)
    PTORemaining = db.Column(db.Integer)
    HoursWorked = db.Column(db.Float)
    DepartmentID = db.Column(db.Integer, db.ForeignKey('department.DepartmentID'))
    ShiftID = db.Column(db.Integer, db.ForeignKey('shift.ShiftID'))

    department = db.relationship('Department', backref='employees')
    shift = db.relationship('Shift', backref='employees')

class DisciplinaryAction(db.Model):
    ActionID = db.Column(db.Integer, primary_key=True)
    EmployeeID = db.Column(db.Integer, db.ForeignKey('employee.EmployeeID'))
    ActionType = db.Column(db.String(100))
    ActionDate = db.Column(db.Date)
    Description = db.Column(db.Text)

    employee = db.relationship('Employee', backref='actions')

class EmployeeCertification(db.Model):
    EmployeeID = db.Column(db.Integer, db.ForeignKey('employee.EmployeeID'), primary_key=True)
    CertificationID = db.Column(db.Integer, db.ForeignKey('certification.CertificationID'), primary_key=True)
    DateObtained = db.Column(db.Date)

    employee = db.relationship('Employee', backref='certifications')
    certification = db.relationship('Certification')
