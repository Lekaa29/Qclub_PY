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
    
    parties = Party.query.filter_by(live=1).all()
    
    return render_template("home.html", parties=parties)

@views.route('/home', methods=["GET", "POST"])
def home():
    all_tables = Table.query.all()
        
    tables = [0 for i in range(23)]
    
    for table in all_tables:
        tables[int(table.id)-1] = table.surname
    
    return render_template("mapq.html", tables=tables)
 
@views.route("/open-party", methods=["POST"])
def open_party():
    partyid = request.form.get("partyid")
    print(partyid)
    party = Party.query.get(partyid)
    
    all_tables = Table.query.filter_by(party_id=partyid).all()
    tables = [0 for i in range(23)]
    
    for table in all_tables:
        tables[int(table.id)-1] = table.surname
        
    return render_template("mapq.html", party=party, tables=tables)
    
    
@views.route('/admin', methods=["GET", "POST"])
def admin():
    if request.method == "GET":
        
        parties2 = Party.query.all()
        
        parties = []
        for party in parties2:
            parties.append(party)
        
        return render_template("admin_home.html", parties=parties)

@views.route("/admin-tables", methods=["GET", "POST"])
def admin_tables():
    partyid = request.args.get("partyid")
    party = Party.query.get(partyid)
    tables = Table.query.filter_by(party_id=partyid).all()
    
    return render_template("admin_tables.html", tables=tables, party=party)

@views.route('/reserve', methods=["GET", "POST"])
def reserve():
    if request.method == "GET":
        clicked_table_index = request.args.get("clickedTableIndex")
        partyid = request.args.get("partyid")

        party = Party.query.get(partyid)
        
        bottles = [
            "Jack Daniels 0.75l 100.00 E",
            "Vigor Vodka 0.75l 75.00 E",
            "Pelinkovac 0.75l 70.00 E",
            "Jägermeister 0.75l 90.00 E",
            "Chivas Regal 12 0.75l 120.00 E",
            "Grey Goose Vodka 0.75l 200.00 E",
            "Hennessy VS Cognac 0.75l 110.00 E",
            "Bombay Sapphire Gin 0.75l 75.00 E",
            "Baileys Irish Cream 0.75l 78.00 E",
            "Patrón Silver Tequila 0.75l 115.00 E"
        ]
        return render_template("addreservation.html", bottles=bottles, party=party, table_index=clicked_table_index)
    else: 
        name = request.form.get("name")
        surname = request.form.get("surname")
        email = request.form.get("email")
        phone = request.form.get("number")
        table_id = request.form.get("clickedTableIndex")
        bottle = request.form.get("selectedBottle")
        partyid = request.form.get("partyid")
        
        party = Party.query.get(partyid)

            
        table = Table.query.get(table_id)
        print(bottle)
        if table:
            return render_template("taken.html")
        else:
            new_table = Table(id=table_id, bottle=bottle, party_id=partyid, taken=1, name=name, surname=surname, email=email, phone=phone)
            db.session.add(new_table)
            db.session.commit()
            
        
        all_tables = Table.query.all()
        
        tables = [0 for i in range(23)]
        
        for table in all_tables:
            tables[int(table.id)-1] = table.surname
        
            
        
               
        return render_template("mapq.html", tables=tables, party=party)

        
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
        
        return redirect(url_for("views.admin"))

@views.route("/edit-party", methods=["GET", "POST"])
def edit_party():
    if request.method == "GET":
        partyid = request.args.get("partyid")
        
        party = Party.query.get(partyid)
        
        return render_template("edit_party.html", party=party)

    else:
        partyid = request.form.get("partyid")
        
        name = request.form.get("name")
        price = request.form.get("price")
        date_str = request.form.get("date")
        bottle = request.form.get("bottle")
        
        party = Party.query.get(partyid)
        
        party.name = name
        party.res_price = price
        party.date = datetime.strptime(date_str, "%Y-%m-%d").date()
        party.bottle = bottle
        db.session.commit()
        
        return redirect(url_for("views.admin"))
    
@views.route("/remove-party", methods=["GET", "POST"])
def del_party():
    if request.method == "GET":
        partyid = request.args.get("partyid")
        
        party = Party.query.get(partyid)
        
        return render_template("delete_party.html", party=party)
    else:
        partyid = request.form.get("partyid")
        
        party = Party.query.get(partyid)
        
        db.session.delete(party)
        db.session.commit()
        
        return redirect(url_for("views.admin"))

@views.route("go-live", methods=["POST"])
def go_live():
    partyid = request.form.get("partyid")    
    party = Party.query.get(partyid)
    party.live = 1
    db.session.commit()
    
    return redirect(url_for("views.admin"))
    
@views.route("stop-live", methods=["POST"])
def stop_live():
    partyid = request.form.get("partyid")
    party = Party.query.get(partyid)
    party.live = 0
    db.session.commit()
    
    return redirect(url_for("views.admin"))