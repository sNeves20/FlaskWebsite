from __future__ import annotations

import json

from flask import Blueprint
from flask import flash
from flask import jsonify
from flask import render_template
from flask import request
from flask_login import current_user
from flask_login import login_required

from . import db
from website.models import Finance


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    if request.method == 'POST':
        finance = request.form.get('finance')

        if len(finance) < 1:
            flash(
                'Finance info incomplete. Please try again',
                category='error',
            )
        else:
            new_finance = Finance(data=finance, user_id=current_user.id)
            db.session.add(new_finance)
            db.session.commit()
            flash('Financial Info Successfully submitted', category='success')

    return render_template('home.html', user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():

    return jsonify({})


@views.route('/delete-info', methods=['POST'])
def delete_info():
    data = json.loads(request.data)
    info_id = data['infoId']
    info = Finance.query.get(info_id)
    if info:
        if info.user_id == current_user.id:
            db.session.delete(info)
            db.session.commit()
            return jsonify({})
