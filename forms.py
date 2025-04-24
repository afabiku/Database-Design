from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField, SelectField, DateField, SubmitField, TimeField, TextAreaField
from wtforms.validators import DataRequired, Optional

class SearchForm(FlaskForm):
    query = StringField('Search by Name or ID', validators=[DataRequired()])
    submit = SubmitField('Search')

class NewEmployeeForm(FlaskForm):
    FirstName = StringField('First Name', validators=[DataRequired()])
    LastName = StringField('Last Name', validators=[DataRequired()])
    StartDate = DateField('Start Date', validators=[Optional()])
    Salary = DecimalField('Salary', validators=[Optional()])
    Status = SelectField('Status', choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time')])
    DepartmentID = IntegerField('Department ID', validators=[Optional()])
    ShiftID = IntegerField('Shift ID', validators=[Optional()])
    submit = SubmitField('Add Employee')

class PTOForm(FlaskForm):
    amount = IntegerField('PTO Amount', validators=[DataRequired()])
    submit_add = SubmitField('Add PTO')
    submit_use = SubmitField('Use PTO')

class CertificationForm(FlaskForm):
    CertificationID = IntegerField('Certification ID', validators=[DataRequired()])
    DateObtained = DateField('Date Obtained', validators=[DataRequired()])
    submit = SubmitField('Grant Certification')

class ActionForm(FlaskForm):
    ActionType = StringField('Action Type', validators=[DataRequired()])
    ActionDate = DateField('Action Date', validators=[DataRequired()])
    Description = TextAreaField('Description', validators=[Optional()])
    submit = SubmitField('Add Action')

class ShiftForm(FlaskForm):
    ShiftID = IntegerField('New Shift ID', validators=[DataRequired()])
    submit = SubmitField('Change Shift')
