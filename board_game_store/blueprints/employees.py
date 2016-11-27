from board_game_store.db.access import add_employee
from board_game_store.models.employee import Employee
from flask import Blueprint, flash, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

employees_blueprint = Blueprint('employee', __name__, template_folder='templates')


class AddEmployeeForm(FlaskForm):
    cpf = StringField('CPF', validators=[DataRequired()])
    name = StringField('Nome', validators=[DataRequired()])
    surname = StringField('Sobrenome', validators=[DataRequired()])
    role = StringField('Função', validators=[DataRequired()])
    salary = StringField('Salário', validators=[DataRequired()])
    supervisor = StringField('CPF do supervisor', validators=[DataRequired()])


@employees_blueprint.route('/employees/add-employee', methods=['GET', 'POST'])
def add_games_page():
    def error(message):
        flash(message)
        return redirect('/error')
    form = AddEmployeeForm()
    if form.validate_on_submit():
        try:
            add_employee(Employee(form.cpf.data, form.name.data, form.surname.data,
                                  form.role.data, form.salary.data, form.supervisor.data))
        except Exception as e:
            import traceback
            return error('Erro no banco de dados: {}'.format(traceback.format_exc()))
        return redirect('success')
    return render_template('employees/add_employee.html', form=form)