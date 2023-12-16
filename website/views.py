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
    
    return render_template("map.html")
    

@views.route('/home')
@login_required
def home():
    return render_template("home.html", user=current_user)

        
    