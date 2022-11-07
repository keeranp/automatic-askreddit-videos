import os
import shutil

def create_folders():
    if os.path.exists("assets"):
        shutil.rmtree(os.path.join("assets","sounds"))
        shutil.rmtree(os.path.join("assets","images"))

    os.makedirs(os.path.join("assets","sounds"))
    os.makedirs(os.path.join("assets","images"))