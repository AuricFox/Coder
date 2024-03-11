from flask import render_template
from flask import current_app as app

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