from flask_login import login_required, current_user
from flask import Blueprint, render_template, request, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 
from flask_login import login_user, login_required, logout_user, current_user
import json
views = Blueprint('views', __name__)


@views.route('/')
def welcome():
    
    return render_template("mapq.html")
    

@views.route('/reserve', methods=["GET", "POST"])
def reserve():
    if request.method == "GET":
        return render_template("addreservation.html")
    else: 
        name = request.form.get("name")
        surname = request.form.get("surname")
        email = request.form.get("email")
        phone = request.form.get("number")
        
        league_id = request.form['leagueid']
        table = Table.query.get(table_id)
        
        return render_template("mapq.html")

        
    