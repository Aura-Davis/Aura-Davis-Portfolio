from flask import Blueprint, render_template, request, jsonify, redirect, url_for
import os

views = Blueprint(__name__, "views")

@views.route("/")
def home():
        return render_template("index.html")

@views.route("/Employee_Management_System")
def Employee_Management_System():
    return render_template("Employee_Management_System.html")