from flask import Flask, render_template, request, redirect, flash, url_for, send_from_directory
import os
import json
import dateutil.parser
from operator import itemgetter, attrgetter
from fsu_physik import common
app = Flask(__name__)
app.secret_key = 'ds_timer'


common.refreshnavigation()
def innocdn_url(path):
    return "https://dsde.innogamescdn.com/8.58/30847" + path

app.jinja_env.globals.update(version="0.1")


@app.route("/static/<path:path>")
def static_files(path):
    return send_from_directory("static", path)

#def sort_unit_dict(dict):
#    units = {"spear":0, "sword":1, "axe":2, "archer":3, "spy":4, "light":5, "marcher":6, "heavy":7, "ram":8, "catapult":9, "knight":10, "snob":11}


@app.route("/")
def index():
    return render_template("erklaerbaer.html")

@app.route("/exercise")
def exercise():
    semester = ""
    course = ""
    files=[]
    if "semester" in request.args:
        semester = request.args.get("semester")
        if "course" in request.args:
            course = request.args.get("course")
            files=common.get_course_files(semester=semester, course=course)
    return render_template("exercise.html",semester=semester, course=course, files=files)

@app.route("/refresh")
def refresh():
    app.jinja_env.globals.update(g_navigation=common.refreshnavigation())
    return render_template("erklaerbaer.html")
