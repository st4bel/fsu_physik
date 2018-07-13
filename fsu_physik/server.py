from flask import Flask, render_template, request, redirect, flash, url_for, send_from_directory
import os
import json
import dateutil.parser
from operator import itemgetter, attrgetter
from fsu_physik import navigation, common#
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.join(common.get_root_folder(),"uploadtest")
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'fsu_physik'

#navigation.get_navigation()
def innocdn_url(path):
    return "https://dsde.innogamescdn.com/8.58/30847" + path

app.jinja_env.globals.update(version="0.1",g_navigation=navigation.get_exercise_tree())

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
            #if semester == "": semester = navigation.get_semester_of_course(course)
            files=navigation.get_course_files(semester=semester, course=course)
    return render_template("exercise.html",semester=semester, course=course, files=files)

@app.route("/refresh")
def refresh():
    app.jinja_env.globals.update(g_navigation=navigation.get_exercise_tree())
    return render_template("erklaerbaer.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',filename=filename))
    return render_template("upload.html")


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
