from __future__ import annotations

from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_login import current_user
from flask_login import login_required


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():

    return render_template('login.html')


@auth.route('/logout')
@login_required
def logout():

    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash(
                'Email must be greater than 3 characters.',
                category='error',
            )
        elif len(first_name) < 2:
            flash(
                'First name must be greater than 1 character.',
                category='error',
            )
        elif password1 != password2:
            flash(
                'Passwords don\'t match.',
                category='error',
            )
        elif len(password1) < 7:
            flash(
                'Password must be at least 7 characters.',
                category='error',
            )
        else:
            flash(
                'Account created!',
                category='success',
            )

    return render_template('sign_up.html', user=current_user)
