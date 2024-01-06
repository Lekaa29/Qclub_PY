from flask_login import login_required, current_user
from flask import Blueprint, render_template, request, redirect, url_for
from .models import User, Table
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db 
from flask_login import login_user, login_required, logout_user, current_user
import json
views = Blueprint('views', __name__)


@views.route('/')
def welcome():
    
    all_tables = Table.query.all()
        
    tables = [0 for i in range(23)]
    
    for table in all_tables:
        tables[int(table.id)-1] = table.surname
    
    return render_template("mapq.html", tables=tables)

@views.route('/home', methods=["GET", "POST"])
def home():
    return redirect(url_for("views.welcome"))
    

@views.route('/reserve', methods=["GET", "POST"])
def reserve():
    if request.method == "GET":
        clicked_table_index = request.args.get("clickedTableIndex")

        return render_template("addreservation.html", table_index=clicked_table_index)
    else: 
        name = request.form.get("name")
        surname = request.form.get("surname")
        email = request.form.get("email")
        phone = request.form.get("number")
        table_id = request.form.get("clickedTableIndex")
        
        for x in request.form.items():
            print(x)
            
        table = Table.query.get(table_id)
        
        if table:
            print(0,table.id,0)
            return render_template("taken.html")
        else:
            new_table = Table(id=table_id, taken=1, name=name, surname=surname, email=email, phone=phone)
            db.session.add(new_table)
            db.session.commit()
            
        
        all_tables = Table.query.all()
        
        tables = [0 for i in range(23)]
        
        for table in all_tables:
            tables[int(table.id)-1] = table.surname
        
        print(tables)
            
        
               
        return render_template("mapq.html", tables=tables)

        
    