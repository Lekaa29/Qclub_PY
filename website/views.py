from flask_login import login_required, current_user
from flask import Blueprint, render_template, request, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db 
from flask_login import login_user, login_required, logout_user, current_user
import json
views = Blueprint('views', __name__)


@views.route('/')
def welcome():
    tables = [0 for i in range(25)]
    
    return render_template("mapq.html", tables=tables)
    

@views.route('/reserve', methods=["GET", "POST"])
def reserve():
    if request.method == "GET":
        return render_template("addreservation.html")
    else: 
        name = request.form.get("name")
        surname = request.form.get("surname")
        email = request.form.get("email")
        phone = request.form.get("number")
        
        table_id = request.form['clickedTableIndex']
        
        tables = [0 for i in range(25)]
        
        return render_template("mapq.html", id=table_id, tables=tables)

        
    