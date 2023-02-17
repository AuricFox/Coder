from flask import Flask, request, redirect, render_template, url_for, jsonify

import os
import sys
sys.path.append('./src/')
import bioinformatics as bio

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
@app.route("/counting_codons", methods=["POST", "GET"])
def counting_codons():
    if(request.method == "GET"):                                    # Render baseline html
        return render_template('bioinformatics/counting_codons.html', nav_id='bio-page', show_id='form')
    else:                                                           # User submitted form data
        file = request.files["file"]                                # Get user's submitted file
        path = os.path.join(os.path.dirname(__file__), "src/temp")  # Path where file will be saved

        if not os.path.exists(path):                                # Checks if path exists
            os.makedirs(path)                                       # Create path if it doesn't exist
        
        file_path = os.path.join(path, file.filename)               # Creating saved file path
        file.save(file_path)                                        # Saving input file
        data = bio.getCodons(file.filename)                         # Get codon and amino acid data
        os.remove(file_path)                                        # File is no longer needed
        
        return render_template('bioinformatics/codon_results.html', nav_id='bio-page', data=data)

# Accessing codon_results Page
@app.route("/codon_results")
def codon_results():
    return render_template('bioinformatics/codon_results.html', nav_id='bio-page')

# ====================================================================
# Subpages of Computer Science
# ====================================================================

# Accessing useful_tools Page
@app.route("/integers")
def integers():
    return render_template('computer_science/integers.html', nav_id="csci-page")

# Accessing useful_tools Page
@app.route("/floats")
def floats():
    return render_template('computer_science/floats.html', nav_id="csci-page")

# Accessing useful_tools Page
@app.route("/dates")
def dates():
    return render_template('computer_science/dates.html', nav_id="csci-page")

# Accessing useful_tools Page
@app.route("/characters")
def characters():
    return render_template('computer_science/characters.html', nav_id="csci-page")

# Accessing useful_tools Page
@app.route("/strings")
def strings():
    return render_template('computer_science/strings.html', nav_id="csci-page")

# Accessing useful_tools Page
@app.route("/booleans")
def booleans():
    return render_template('computer_science/booleans.html', nav_id="csci-page")

# Accessing useful_tools Page
@app.route("/nulls")
def nulls():
    return render_template('computer_science/nulls.html', nav_id="csci-page")

# Accessing useful_tools Page
@app.route("/data_types")
def data_types():
    return render_template('computer_science/data_types.html', nav_id="csci-page")

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
