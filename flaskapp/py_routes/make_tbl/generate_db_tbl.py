from flask import Blueprint, render_template, jsonify, request, redirect, url_for
from flask_login import login_required

from flaskapp import db, run_dammit

generate = Blueprint('generate', __name__, template_folder='gen_template')

app = run_dammit()
# from . import generate

@generate.route('/create_tbl', methods=['GET', 'POST'])
def create_tbl():
    if request.method == 'GET':
        with app.test_request_context():
            db.create_all()
            
            page_title = 'All tables have been created.'
            return render_template('hud.html', page_title=page_title)




