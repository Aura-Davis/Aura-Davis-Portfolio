from flask import Blueprint, render_template, request, jsonify, redirect, url_for
import os

views = Blueprint(__name__, "views")

@views.route("/")
def home():
        return render_template("index.html")

@views.route("/Employee_Management_System")
def Employee_Management_System():
    return render_template("Employee_Management_System.html")

@views.route("/Aura_Ecommerce")
def Aura_Ecommerce():
    return render_template("Aura_Ecommerce.html")

@views.route("/AI_Text_Generator")
def AI_Text_Generator():
    return render_template("AI_Text_Generator.html")

@views.route("/Password_Manager")
def Password_Manager():
    return render_template("Password_Manager.html")