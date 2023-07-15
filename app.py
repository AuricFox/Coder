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
    return render_template('data_structures.html', nav_id="struct-page")

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

# Custom page not found
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', nav_id="home-page"), 404

# Custom page not found
@app.errorhandler(500)
def server_error(error):
    return render_template('404.html', nav_id="home-page"), 404

# ====================================================================
# Subpages of Data Types [REMOVE]
# ====================================================================

@app.route('/data_types/<path:pagename>')
def datatypes_route(pagename):
    if pagename == 'Main':
        return render_template('data_types.html', nav_id="data-page")
    elif pagename == 'integers':
        return render_template('data_types/integers.html', nav_id="data-page")
    elif pagename == 'floats':
        return render_template('data_types/floats.html', nav_id="data-page")
    elif pagename == 'dates':
        return render_template('data_types/dates.html', nav_id="data-page")
    elif pagename == 'characters':
        return render_template('data_types/characters.html', nav_id="data-page")
    elif pagename == 'strings':
        return render_template('data_types/strings.html', nav_id="data-page")
    elif pagename == 'booleans':
        return render_template('data_types/booleans.html', nav_id="data-page")
    elif pagename == 'nulls':
        return render_template('data_types/nulls.html', nav_id="data-page")
    else:
        return render_template('404.html', nav_id="data-page")

# ====================================================================
# Subpages of Data Structures
# ====================================================================

@app.route('/data_structures/<path:pagename>')
def datastructure_route(pagename):
    if pagename == 'Main':
        return render_template('data_structures.html', nav_id="struct-page")
    elif pagename == 'arrays':
        return render_template('data_structures/arrays.html', nav_id="struct-page")
    elif pagename == 'linked_lists':
        return render_template('data_structures/linked_lists.html', nav_id="struct-page")
    elif pagename == 'queues':
        return render_template('data_structures/queues.html', nav_id="struct-page")
    elif pagename == 'stacks':
        return render_template('data_structures/stacks.html', nav_id="struct-page")
    elif pagename == 'hash_tables':
        return render_template('data_structures/hash_tables.html', nav_id="struct-page")
    else:
        return render_template('404.html', nav_id="struct-page")

# ====================================================================
# Subpages of Data Algorithms
# ====================================================================



# ====================================================================
# Subpages of Programming Languages
# ====================================================================



# ====================================================================
# Subpages of C [Programming Languages]
# ====================================================================

# Accessing C Main Page
@app.route("/c")
def c():
    return render_template('languages/c/c.html', nav_id="lang-page")

@app.route('/c/<path:pagename>')
def c_route(pagename):
    print(pagename)
    if pagename == 'Main':
        return render_template('languages/c/c.html', nav_id="lang-page")
    elif pagename == 'Setup':
        return render_template('languages/c/c_setup.html', nav_id="lang-page")
    elif pagename == 'Comments':
        return render_template('languages/c/c_comments.html', nav_id="lang-page")
    elif pagename == 'Data_Types':
        return render_template('languages/c/c_data_types.html', nav_id="lang-page")
    elif pagename == 'Constants':
        return render_template('languages/c/c_constants.html', nav_id="lang-page")
    elif pagename == 'Operators':
        return render_template('languages/c/c_operators.html', nav_id="lang-page")
    else:
        return render_template('404.html', nav_id="lang-page")

# ====================================================================
# Subpages of C++ [Programming Languages]
# ====================================================================

# Accessing C++ Main Page
@app.route("/cpp")
def cpp():
    return render_template('languages/cpp/cpp.html', nav_id="lang-page")

@app.route('/cpp/<path:pagename>')
def cpp_route(pagename):
    if pagename == 'Main':
        return render_template('languages/cpp/cpp.html', nav_id="lang-page")
    elif pagename == 'Setup':
        return render_template('languages/cpp/cpp_setup.html', nav_id="lang-page")
    else:
        return render_template('404.html', nav_id="lang-page")
        
# ====================================================================
# Subpages of C# [Programming Languages]
# ====================================================================

# Accessing C# Main Page
@app.route("/cs")
def cs():
    return render_template('languages/cs/cs.html', nav_id="lang-page")

@app.route('/cs/<path:pagename>')
def cs_route(pagename):
    if pagename == 'Main':
        return render_template('languages/cs/cs.html', nav_id="lang-page")
    elif pagename == 'Setup':
        return render_template('languages/cs/cs_setup.html', nav_id="lang-page")
    else:
        return render_template('404.html', nav_id="lang-page")

# ====================================================================
# Subpages of Java [Programming Languages]
# ====================================================================

# Accessing Java Main Page
@app.route("/java")
def java():
    return render_template('languages/java/java.html', nav_id="lang-page")

@app.route('/java/<path:pagename>')
def java_route(pagename):
    if pagename == 'Main':
        return render_template('languages/java/java.html', nav_id="lang-page")
    else:
        return render_template('404.html', nav_id="lang-page")

# ====================================================================
# Subpages of JavaScript [Programming Languages]
# ====================================================================

# Accessing JavaScript Main Page
@app.route("/javascript")
def javascript():
    return render_template('languages/javascript/javascript.html', nav_id="lang-page")

@app.route('/javascript/<path:pagename>')
def javascript_route(pagename):
    if pagename == 'Main':
        return render_template('languages/javascript/javascript.html', nav_id="lang-page")
    else:
        return render_template('404.html', nav_id="lang-page")

# ====================================================================
# Subpages of Python [Programming Languages]
# ====================================================================

# Accessing Python Main Page
@app.route("/python")
def python():
    return render_template('languages/python/python.html', nav_id="lang-page")

@app.route('/python/<path:pagename>')
def python_route(pagename):
    print(pagename)
    if pagename == 'Main':
        return render_template('languages/python/python.html', nav_id="lang-page")
    elif pagename == 'Setup':
        return render_template('languages/python/py_setup.html', nav_id="lang-page")
    elif pagename == 'Lambda':
        return render_template('languages/python/py_lambda.html', nav_id="lang-page")
    else:
        return render_template('404.html', nav_id="lang-page")

# ====================================================================
# Subpages of HTML [Programming Languages]
# ====================================================================

# Accessing HTML Main Page
@app.route("/html")
def html():
    return render_template('languages/html/html.html', nav_id="lang-page")

@app.route('/html/<path:pagename>')
def html_route(pagename):
    if pagename == 'Main':
        return render_template('languages/html/html.html', nav_id="lang-page")
    else:
        return render_template('404.html', nav_id="lang-page")

# ====================================================================
# Subpages of CSS [Programming Languages]
# ====================================================================

# Accessing CSS Main Page
@app.route("/css")
def css():
    return render_template('languages/css/css.html', nav_id="lang-page")

@app.route('/css/<path:pagename>')
def css_route(pagename):
    if pagename == 'Main':
        return render_template('languages/css/css.html', nav_id="lang-page")
    else:
        return render_template('404.html', nav_id="lang-page")

# ====================================================================
# Subpages of SQL [Programming Languages]
# ====================================================================

# Accessing SQL Main Page
@app.route("/sql")
def sql():
    return render_template('languages/sql/sql.html', nav_id="lang-page")

@app.route('/sql/<path:pagename>')
def sql_route(pagename):
    if pagename == 'Main':
        return render_template('languages/sql/sql.html', nav_id="lang-page")
    else:
        return render_template('404.html', nav_id="lang-page")

# ====================================================================
# Subpages of Math
# ====================================================================


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
# Subpages of Bioinformatics [Useful Tools]
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
# Run Main
# ====================================================================
if __name__ == "__main__":
    app.run()
