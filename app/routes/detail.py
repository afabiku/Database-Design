from flask import Blueprint, render_template, url_for, redirect
from app.forms import PTOForm, CertificationForm, ActionForm, ShiftForm
from app.models import EmployeeCertification, Employee, DisciplinaryAction
from app import db

bp = Blueprint("detail", __name__)

@bp.route('/employee/<int:employee_id>', methods=['GET', 'POST'])
def index(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    pto_form = PTOForm()
    cert_form = CertificationForm()
    action_form = ActionForm()
    shift_form = ShiftForm()

    if pto_form.submit_add.data and pto_form.validate():
        employee.ptoremaining += pto_form.amount.data
        db.session.commit()
        return redirect(url_for('detail.index', employee_id=employee_id))

    if pto_form.submit_use.data and pto_form.validate():
        employee.ptoused += pto_form.amount.data
        employee.ptoremaining -= pto_form.amount.data
        db.session.commit()
        return redirect(url_for('detail.index', employee_id=employee_id))

    if cert_form.validate_on_submit():
        new_cert = EmployeeCertification(
            employeeid=employee_id,
            certificationid=cert_form.CertificationID.data,
            dateobtained=cert_form.DateObtained.data
        )
        db.session.add(new_cert)
        db.session.commit()
        return redirect(url_for('detail.index', employee_id=employee_id))

    if action_form.validate_on_submit():
        new_action = DisciplinaryAction(
            employeeid=employee_id,
            actiontype=action_form.ActionType.data,
            actiondate=action_form.ActionDate.data,
            description=action_form.Description.data
        )
        db.session.add(new_action)
        db.session.commit()
        return redirect(url_for('detail.index', employee_id=employee_id))

    if shift_form.validate_on_submit():
        employee.shiftid = shift_form.ShiftID.data
        db.session.commit()
        return redirect(url_for('detail.index', employee_id=employee_id))

    return render_template('employee_detail.html', employee=employee,
                           pto_form=pto_form, cert_form=cert_form,
                           action_form=action_form, shift_form=shift_form)