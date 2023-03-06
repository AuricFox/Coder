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

# Accessing useful_tools Page
@app.route("/data_types")
def data_types():
    return render_template('data_types.html', nav_id="data-page")

# Accessing useful_tools Page
@app.route("/data_structures")
def data_structures():
    return render_template('data_types.html', nav_id="struct-page")

# Accessing engineering Page
@app.route("/languages")
def languages():
    return render_template('languages.html', nav_id="lang-page")

# Accessing algorithms Page
@app.route("/algorithms")
def algorithms():
    return render_template('algorithms.html', nav_id="algo-page")

# Accessing math Page
@app.route("/math")
def math():
    return render_template('math.html', nav_id="math-page")

# Accessing useful_tools Page
@app.route("/useful_tools")
def useful_tools():
    return render_template('useful_tools.html', nav_id="tools-page")

# Accessing tutorials Page
@app.route("/tutorials")
def tutorials():
    return render_template('tutorials.html', nav_id="info-page")

# ====================================================================
# Subpages of Bioinformatics
# ====================================================================

# Accessing counting_codons Page
@app.route("/counting_codons", methods=["POST", "GET"])
def counting_codons():
    if(request.method == "GET"):                                    # Render baseline html
        return render_template('useful_tools/bioinformatics/counting_codons.html', nav_id='tools-page', show_id='form')
    else:                                                           # User submitted form data
        file = request.files["file"]                                # Get user's submitted file
        path = os.path.join(os.path.dirname(__file__), "src/temp")  # Path where file will be saved

        if not os.path.exists(path):                                # Checks if path exists
            os.makedirs(path)                                       # Create path if it doesn't exist
        
        file_path = os.path.join(path, file.filename)               # Creating saved file path
        file.save(file_path)                                        # Saving input file
        data = bio.getCodons(file.filename)                         # Get codon and amino acid data
        os.remove(file_path)                                        # File is no longer needed
        
        return render_template('useful_tools/bioinformatics/codon_results.html', nav_id='tools-page', data=data)

# Accessing codon_results Page
@app.route("/codon_results")
def codon_results():
    return render_template('useful_tools/bioinformatics/codon_results.html', nav_id='tools-page')

# ====================================================================
# Subpages of Tutorials [Data Types]
# ====================================================================

# Accessing useful_tools Page
@app.route("/integers")
def integers():
    return render_template('data_types/integers.html', nav_id="data-page")

# Accessing useful_tools Page
@app.route("/floats")
def floats():
    return render_template('data_types/floats.html', nav_id="data-page")

# Accessing useful_tools Page
@app.route("/dates")
def dates():
    return render_template('data_types/dates.html', nav_id="data-page")

# Accessing useful_tools Page
@app.route("/characters")
def characters():
    return render_template('data_types/characters.html', nav_id="data-page")

# Accessing useful_tools Page
@app.route("/strings")
def strings():
    return render_template('data_types/strings.html', nav_id="data-page")

# Accessing useful_tools Page
@app.route("/booleans")
def booleans():
    return render_template('data_types/booleans.html', nav_id="data-page")

# Accessing useful_tools Page
@app.route("/nulls")
def nulls():
    return render_template('data_types/nulls.html', nav_id="data-page")

# ====================================================================
# Subpages of Useful Tools 
# ====================================================================

# Accessing Bioinformatics Page
@app.route("/bioinformatics")
def bioinformatics():
    return render_template('useful_tools/bioinformatics.html', nav_id="tools-page")

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
