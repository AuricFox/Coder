from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__, static_folder='static')

# ====================================================================
# Accessing Home page
@app.route("/")
def home():
    return render_template('home.html')

# Accessing Bioinformatics Page
@app.route("/bioinformatics")
def bioinformatics():
    return render_template('bioinformatics.html')

# Accessing chemistry Page
@app.route("/chemistry")
def chemistry():
    return render_template('chemistry.html')

# Accessing computer_science Page
@app.route("/computer_science")
def computer_science():
    return render_template('computer_science.html')

# Accessing engineering Page
@app.route("/engineering")
def engineering():
    return render_template('engineering.html')

# Accessing math Page
@app.route("/math")
def math():
    return render_template('math.html')

# Accessing useful_tools Page
@app.route("/useful_tools")
def useful_tools():
    return render_template('useful_tools.html')

# ====================================================================
# Uploading files sent by user
'''
@app.route("/upload", methods=["POST"])
def upload():
    files = request.files.getlist("files")
    for file in files:
        file.save("path/to/save/file")
    return "Files uploaded successfully"
'''

if __name__ == "__main__":
    app.run()
