import csv
import logging
import os

from flask import Blueprint, render_template, abort, url_for,current_app
from flask_login import current_user, login_required
from jinja2 import TemplateNotFound

from app.db import db
from app.db.models import Song
from app.songs.forms import csv_upload
from werkzeug.utils import secure_filename, redirect

transaction = Blueprint('transaction', __name__,
                        template_folder='templates')

@transaction.route('/songs', methods=['GET'], defaults={"page": 1})
@transaction.route('/songs/<int:page>', methods=['GET'])
def transaction_browse(page):
    page = page
    per_page = 1000
    pagination = transaction.query.paginate(page, per_page, error_out=False)
    data = pagination.items
    try:
        return render_template('browse_transaction.html',data=data,pagination=pagination)
    except TemplateNotFound:
        abort(404)