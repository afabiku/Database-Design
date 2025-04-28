from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, DecimalField, DateField, TextAreaField
from wtforms.validators import DataRequired, Optional
from wtforms.validators import Optional
from app.models import Certification, Department, Shift

class SearchForm(FlaskForm):
    query = StringField('Name or ID', validators=[Optional()])
    certification = SelectField('Certification', coerce=int, choices=[], validators=[Optional()])
    department = SelectField('Department', coerce=int, choices=[], validators=[Optional()])
    status = SelectField('Status', choices=[
        ('', 'Any'), 
        ('Full-Time', 'Full-Time'), 
        ('Part-Time', 'Part-Time')
    ], validators=[Optional()])
    shift = SelectField('Shift', coerce=int, choices=[], validators=[Optional()])
    submit = SubmitField('Search')

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.certification.choices = [(0, 'Any')] + [(c.certificationid, c.certificationname) for c in Certification.query.all()]
        self.department.choices = [(0, 'Any')] + [(d.departmentid, d.departmentname) for d in Department.query.all()]
        self.shift.choices = [(0, 'Any')] + [(s.shiftid, s.name) for s in Shift.query.all()]

class NewEmployeeForm(FlaskForm):
    FirstName = StringField('First Name', validators=[DataRequired()])
    LastName = StringField('Last Name', validators=[DataRequired()])
    StartDate = DateField('Start Date', validators=[Optional()])
    Salary = DecimalField('Salary', validators=[Optional()])
    Status = SelectField('Status', choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time')])
    DepartmentID = SelectField('Department', coerce=int, validators=[DataRequired()])
    ShiftID = SelectField('Shift', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Add Employee')

    def __init__(self, *args, **kwargs):
        super(NewEmployeeForm, self).__init__(*args, **kwargs)
        self.DepartmentID.choices = [(d.departmentid, d.departmentname) for d in Department.query.all()]
        self.ShiftID.choices = [(s.shiftid, s.name) for s in Shift.query.all()]


class PTOForm(FlaskForm):
    amount = IntegerField('PTO Amount', validators=[DataRequired()])
    submit_add = SubmitField('Add PTO')
    submit_use = SubmitField('Use PTO')


class CertificationForm(FlaskForm):
    CertificationID = SelectField('Certification', coerce=int, validators=[DataRequired()])
    DateObtained = DateField('Date Obtained', validators=[DataRequired()])
    submit = SubmitField('Grant Certification')

    def __init__(self, *args, **kwargs):
        super(CertificationForm, self).__init__(*args, **kwargs)
        self.CertificationID.choices = [(c.certificationid, c.certificationname) for c in Certification.query.all()]

class ShiftForm(FlaskForm):
    ShiftID = SelectField('Shift', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Change Shift')

    def __init__(self, *args, **kwargs):
        super(ShiftForm, self).__init__(*args, **kwargs)
        self.ShiftID.choices = [(s.shiftid, s.name) for s in Shift.query.all()]

class ActionForm(FlaskForm):
    ActionType = StringField('Action Type', validators=[DataRequired()])
    ActionDate = DateField('Action Date', validators=[DataRequired()])
    Description = TextAreaField('Description', validators=[Optional()])
    submit = SubmitField('Add Action')
