from __future__ import annotations

from flask import Blueprint
from flask import jsonify
from flask import render_template
from flask_login import login_required

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    return render_template('home.html')


@views.route('/delete-note', methods=['POST'])
def delete_note():

    return jsonify({})
