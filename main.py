from flask import Flask, render_template, flash, request, redirect, url_for

import utils as m
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"

results = []
path = ''

app.config['UPLOAD_FOLDER'] = r"static"

def wipe():
    global results
    global path
    results = []
    if path:
        os.remove(path)
        path = ''
    print("Wiped.")

@app.route('/', methods = ["GET", "POST"])
def home():
    global results
    global path
    filename = None

    if request.method == 'POST':
        print("Recieved an image.")
        if 'file' not in request.files:
            flash('No file part')
            print("file not in request.files")
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash("No selected file")
            print("No selected file")
            return redirect(request.url)
        if file:
            filename = file.filename
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            print("Saving to system.")

            result = m.query(path)
            result = m.cleanResult(result)
            print(result)
            results.append(result)

    return render_template("home.html", results=results, file=filename)

@app.route('/bounce')
def bounce():
    wipe()
    return redirect('/')


if __name__ == "__main__":
    #m.configure()
    app.run(host="0.0.0.0", debug=True)