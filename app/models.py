from app import db

#   From Brians Branch
class Department(db.Model):
    __tablename__ = 'department'
    departmentid = db.Column(db.Integer, primary_key=True)
    departmentname = db.Column(db.String(100), nullable=False)

class Shift(db.Model):
    __tablename__ = 'shift'
    shiftid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    daysworked = db.Column(db.String(100))

class Certification(db.Model):
    __tablename__ = 'certification'
    certificationid = db.Column(db.Integer, primary_key=True)
    certificationname = db.Column(db.String(100))
    description = db.Column(db.Text)

class Employee(db.Model):
    __tablename__ = 'employee'
    employeeid = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    startdate = db.Column(db.Date)
    salary = db.Column(db.Float)
    status = db.Column(db.String(20))
    yearsatcompany = db.Column(db.Integer)
    strikes = db.Column(db.Integer)
    ptoused = db.Column(db.Integer)
    ptoremaining = db.Column(db.Integer)
    hoursworked = db.Column(db.Float)
    departmentid = db.Column(db.Integer, db.ForeignKey('department.departmentid'))
    shiftid = db.Column(db.Integer, db.ForeignKey('shift.shiftid'))

    department = db.relationship('Department', backref='employees')
    shift = db.relationship('Shift', backref='employees')

class DisciplinaryAction(db.Model):
    __tablename__ = 'disciplinaryaction'
    actionid = db.Column(db.Integer, primary_key=True)
    employeeid = db.Column(db.Integer, db.ForeignKey('employee.employeeid'))
    actiontype = db.Column(db.String(100))
    actiondate = db.Column(db.Date)
    description = db.Column(db.Text)

    employee = db.relationship('Employee', backref='actions')

class EmployeeCertification(db.Model):
    __tablename__ = 'employeecertification'
    employeeid = db.Column(db.Integer, db.ForeignKey('employee.employeeid'), primary_key=True)
    certificationid = db.Column(db.Integer, db.ForeignKey('certification.certificationid'), primary_key=True)
    dateobtained = db.Column(db.Date)

    employee = db.relationship('Employee', backref='certifications')
    certification = db.relationship('Certification')