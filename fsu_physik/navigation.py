import os



def get_exercise_tree():
    nav = {}
    exercise_path =  os.path.join(os.path.expanduser("~"), ".fsu_physik", "exercise")
    for semester in os.listdir(exercise_path):
        if os.path.isdir(os.path.join(exercise_path, semester)):
            nav[semester]={}
            for course in os.listdir(os.path.join(exercise_path, semester)):
                if os.path.isdir(os.path.join(exercise_path, semester, course)):
                    nav[semester][course]=[]
                    for file in os.listdir(os.path.join(exercise_path, semester, course)):
                        if os.path.isfile(os.path.join(exercise_path, semester, course, file)):
                            nav[semester][course].append(split_coursename(file))
                    if nav[semester][course]==[]:
                        nav[semester][course].append(emptycourse())
    return nav
def split_coursename(coursename):
    f={}
    try:
        f["matrikel"], f["dozent"], f["typ"], f["nummer"] = coursename.split(".")[0].split("_")
    except ValueError:
        f["matrikel"], f["dozent"], f["typ"], f["nummer"] = coursename.split(".")[0],"","",""
    return f
def emptycourse():
    f = {}
    f["matrikel"], f["dozent"], f["typ"], f["nummer"] = "es konnten keine Dateien gefunden werden","","",""
    return f

def get_course_files(semester, course):
    if semester == "": semester = get_semester_of_course(course)
    files = []
    course_path = os.path.join(os.path.expanduser("~"), ".fsu_physik", "exercise", semester, course)
    for file in os.listdir(course_path):
        if os.path.isfile(os.path.join(course_path, file)):
            f={}
            try:
                f["matrikel"], f["dozent"], f["typ"], f["nummer"] = file.split(".")[0].split("_")
            except ValueError:
                f["matrikel"], f["dozent"], f["typ"], f["nummer"] = file.split(".")[0],"","",""
            files.append(f)
    if files == []:
        f = {}
        f["matrikel"], f["dozent"], f["typ"], f["nummer"] = "es konnten keine Dateien gefunden werden","","",""
        files.append(f)
    return files

def get_semester_of_course(course):
    nav = get_navigation()
    for dir in nav:
        for course_dir in dir["sub"]:
            if course_dir == course:
                return dir["name"]

    return ""
def get_navigation():
    navigation = []
    exercise_path = os.path.join(os.path.expanduser("~"), ".fsu_physik", "exercise")
    #create navigation-tree
    for dir in os.listdir(exercise_path):
        if os.path.isdir(os.path.join(exercise_path, dir)):
            subnavigation = {}
            subnavigation["name"] = dir
            subnavigation["sub"] = []
            #if dir == request.args.get("semester"):
            for subdir in os.listdir(os.path.join(exercise_path, dir)):
                if os.path.isdir(os.path.join(exercise_path, dir, subdir)):
                    subnavigation["sub"].append(subdir)

            navigation.append(subnavigation)
    return navigation
    #app.jinja_env.globals.update(g_navigation=navigation)
