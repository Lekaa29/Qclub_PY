from flask_login import login_required, current_user
from flask import Blueprint, render_template, request, redirect, url_for
from .models import User, Table, Party
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db 
from flask_login import login_user, login_required, logout_user, current_user
import json
from datetime import datetime

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
    
@views.route('/admin', methods=["GET", "POST"])
def admin():
    if request.method == "GET":
        
        parties2 = Party.query.all()
        
        parties = []
        for party in parties2:
            parties.append(party)
        
        return render_template("admin_home.html", parties=parties)

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

        
@views.route("/add-party", methods=["GET", "POST"])
def add_party():
    if request.method == "GET":
        return render_template("add_party.html")
    else:
        name = request.form.get("name")
        price = request.form.get("price")
        date_str = request.form.get("date")
        bottle = request.form.get("bottle")
        
        date = datetime.strptime(date_str, '%Y-%m-%d').date()

        if bottle == "yes":
            bottle_bool = 1
        else:
            bottle_bool = 0
        
        new_party = Party(name=name,res_price=price,date=date,bottle=bottle_bool)
        db.session.add(new_party)
        db.session.commit()
            
        print(name,price,date,bottle)
        
        return redirect(url_for("views.welcome"))
        