from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField, SelectField, DateField, SubmitField, TimeField, TextAreaField
from wtforms.validators import DataRequired, Optional

from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, IntegerField, DateField
from wtforms.validators import DataRequired
from models import Certification, Shift


class SearchForm(FlaskForm):
    query = StringField('Search by Name or ID', validators=[DataRequired()])
    submit = SubmitField('Search')

from models import Department, Shift

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
