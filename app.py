from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__, static_folder='static')

# ====================================================================
# Main Pages
# ====================================================================

# Accessing Home page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', nav_id="home-page")

# Accessing Bioinformatics Page
@app.route("/bioinformatics")
def bioinformatics():
    return render_template('bioinformatics.html', nav_id="bio-page")

# Accessing chemistry Page
@app.route("/chemistry")
def chemistry():
    return render_template('chemistry.html', nav_id="chem-page")

# Accessing computer_science Page
@app.route("/computer_science")
def computer_science():
    return render_template('computer_science.html', nav_id="csci-page")

# Accessing engineering Page
@app.route("/engineering")
def engineering():
    return render_template('engineering.html', nav_id="eng-page")

# Accessing math Page
@app.route("/math")
def math():
    return render_template('math.html', nav_id="math-page")

# Accessing useful_tools Page
@app.route("/useful_tools")
def useful_tools():
    return render_template('useful_tools.html', nav_id="tools-page")

# ====================================================================
# Subpages of Bioinformatics
# ====================================================================

# Accessing counting_codons Page
@app.route("/counting_codons")
def counting_codons():
    return render_template('bioinformatics/counting_codons.html', nav_id='bio-page')

# ====================================================================
# Subpages of Computer Science
# ====================================================================

# Accessing useful_tools Page
@app.route("/cs_concepts")
def cs_concepts():
    return render_template('computer_science/cs_concepts.html')

# ====================================================================
# Subpages of Useful Tools 
# ====================================================================

# Accessing useful_tools Page
@app.route("/taxes")
def taxes():
    return render_template('useful_tools/taxes.html', nav_id="tools-page")

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
