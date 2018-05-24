import os

USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36"

def get_root_folder():
    return os.path.join(os.path.expanduser("~"), ".fsu_physik")

def create_folder_structure():
    """Create all folders in the user's home directory.
    """
    root = get_root_folder()
    os.makedirs(root, exist_ok=True)
    folders = ["exercise", "logs"]
    for folder in folders:
        os.makedirs(os.path.join(root, folder), exist_ok=True)

def refreshnavigation():
    navigation = []
    exercise_path = os.path.join(os.path.expanduser("~"), ".fsu_physik", "exercise")
    #create navigation-tree
    for dir in os.listdir(exercise_path):
        if os.path.isdir(os.path.join(exercise_path, dir)):
            subnavigation = {}
            subnavigation["name"] = dir
            subnavigation["sub"] = []
            if dir == request.args.get("semester"):
                for subdir in os.listdir(os.path.join(exercise_path, dir)):
                    if os.path.isdir(os.path.join(exercise_path, dir, subdir)):
                        subnavigation["sub"].append(subdir)

            navigation.append(subnavigation)
    return navigation
    #app.jinja_env.globals.update(g_navigation=navigation)
def get_course_files(course):
    files = []
    course_path = os.path.join(os.path.expanduser("~"), ".fsu_physik", "exercise", course)
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
