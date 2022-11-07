import os
import shutil

def create_folders():
    if os.path.exists("assets"):
        shutil.rmtree("assets")

    os.makedirs(os.path.join("assets","sounds"))
    os.makedirs(os.path.join("assets","images"))