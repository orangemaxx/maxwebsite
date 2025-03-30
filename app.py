from flask import Flask, render_template, url_for, redirect
import os
import json
import shutil
from flask_compress import Compress

with open('pages.json', "r") as file:
    pages = json.load(file)

# Create app and compress
app = Flask(__name__)
compress = Compress()
compress.init_app(app)

# Set the paths for the app
relPath = os.path.dirname(__file__)
buildDir = relPath + "/build/"
if not os.path.exists(buildDir):
    os.makedirs(buildDir)
shutil.copytree("bootstrap/dist/js", "static/js", dirs_exist_ok=True)
shutil.copytree("static/", "build/static", dirs_exist_ok=True)

@app.errorhandler(404)
def serverPage(e):
    return "Whoops! View your generated website in the /build/ directory!", 404

def save_file(filename, args, template):
    with open(buildDir + filename, "w") as f:
        f.write(render_template("pages/" + template, **args))

# app.run(debug=True) # Only use for debugging purposes. Disable before push.