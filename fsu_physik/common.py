import os

USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36"

def get_root_folder():
    #return os.path.join(os.path.expanduser("~"), ".fsu_physik")
    return os.path.join("C:/","xampp","htdocs","fsu_physik")

def create_folder_structure():
    """Create all folders in the user's home directory.
    """
    root = get_root_folder()
    os.makedirs(root, exist_ok=True)
    folders = ["exercise", "logs","uploadtest"]
    for folder in folders:
        os.makedirs(os.path.join(root, folder), exist_ok=True)

def get_static_href():
    return "http://localhost/fsu_physik/exercise/"
