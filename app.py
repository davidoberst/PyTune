import os
import platform
import webview

class API :
 def searchMP3(self):
    system = platform.system()
    user_home = os.path.expanduser("~")

    if system == "Windows":
        folders = ["Downloads"]
    else:
        folders = ["Descargas",
                   "Downloads"]
    found = []
    for folder in folders:
        route = os.path.join(user_home, folder)
        if os.path.exists(route):
            for root, _, files in os.walk(route):
                for f in files:
                    if f.lower().endswith(".mp3"):
                        print(os.path.join(root, f))
                        found = True
                        
    if (not found) :
        return["no files found"]          
    return found 
 
if __name__ == "__main__":
     api = API()
     window = webview.create_window(
         "PyTunes",
         "index.html",
         width =600,
         height=400,
         resizable=False,
         js_api=api

     )
     
     
     webview.start() 

                                


