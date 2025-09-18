import os
import platform

def searchMP3():
    system = platform.system()
    user_home = os.path.expanduser("~")

    if system == "Windows":
        folders = ["Downloads"]
    else:
        folders = ["Descargas",
                   "Downloads"]
    found = False
    for folder in folders:
        route = os.path.join(user_home, folder)
        if os.path.exists(route):
            for root, _, files in os.walk(route):
                for f in files:
                    if f.lower().endswith(".mp3"):
                        print(os.path.join(root, f))
                        found = True
    import os
import platform

def searchMP3():
    system = platform.system()
    user_home = os.path.expanduser("~")

    if system == "Windows":
        folders = ["Downloads"]
    else:
        folders = ["Descargas",
                   "Downloads"]
    found = False
    for folder in folders:
        route = os.path.join(user_home, folder)
        if os.path.exists(route):
            for root, _, files in os.walk(route):
                for f in files:
                    if f.lower().endswith(".mp3"):
                        print(os.path.join(root, f))
                        found = True
                        
    if (not found) :
        print("no files founded")           
                                
searchMP3()
