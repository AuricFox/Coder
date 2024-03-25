from flask import render_template
from app.languages import bp

# Routes for pages associated with data structures

@bp.route("/")
def index():
    return render_template('languages.html', nav_id="lang-page")

# ====================================================================
# Subpages of C [Programming Languages]
# ====================================================================
@bp.route("/c")
def c():
    return render_template('languages/c/c.html', nav_id="lang-page")

@bp.route('/c/setup')
def c_setup():
    return render_template('languages/c/c_setup.html', nav_id="lang-page")

@bp.route('/c/comments')
def c_comments():
    return render_template('languages/c/c_comments.html', nav_id="lang-page")

@bp.route('/c/data_types')
def c_data_types():
    return render_template('languages/c/c_data_types.html', nav_id="lang-page")

@bp.route('/c/constants')
def c_constants():
    return render_template('languages/c/c_constants.html', nav_id="lang-page")

@bp.route('/c/operators')
def c_operators():
    return render_template('languages/c/c_operators.html', nav_id="lang-page")

@bp.route('/c/booleans')
def c_booleans():
    return render_template('languages/c/c_booleans.html', nav_id="lang-page")

@bp.route('/c/conditionals')
def c_conditionals():
    return render_template('languages/c/c_conditionals.html', nav_id="lang-page")

@bp.route('/c/switch_case')
def c_switch_case():
    return render_template('languages/c/c_switch_case.html', nav_id="lang-page")

@bp.route('/c/loops')
def c_loops():
    return render_template('languages/c/c_loops.html', nav_id="lang-page")

@bp.route('/c/arrays')
def c_arrays():
    return render_template('languages/c/c_arrays.html', nav_id="lang-page")

@bp.route('/c/pointers')
def c_pointers():
    return render_template('languages/c/c_pointers.html', nav_id="lang-page")

# ====================================================================
# Subpages of C++ [Programming Languages]
# ====================================================================
@bp.route("/cpp")
def cpp():
    return render_template('languages/cpp/cpp.html', nav_id="lang-page")

@bp.route('/cpp/setup')
def cpp_setup():
    return render_template('languages/cpp/cpp_setup.html', nav_id="lang-page")
        
# ====================================================================
# Subpages of C# [Programming Languages]
# ====================================================================
@bp.route("/cs")
def cs():
    return render_template('languages/cs/cs.html', nav_id="lang-page")

@bp.route('/cs/setup')
def cs_setup():
    return render_template('languages/cs/cs_setup.html', nav_id="lang-page")

# ====================================================================
# Subpages of Java [Programming Languages]
# ====================================================================
@bp.route("/java")
def java():
    return render_template('languages/java/java.html', nav_id="lang-page")

# ====================================================================
# Subpages of JavaScript [Programming Languages]
# ====================================================================
@bp.route("/javascript")
def javascript():
    return render_template('languages/javascript/javascript.html', nav_id="lang-page")

# ====================================================================
# Subpages of Python [Programming Languages]
# ====================================================================
@bp.route("/python")
def python():
    return render_template('languages/python/python.html', nav_id="lang-page")

@bp.route('/python/setup')
def python_setup():
    return render_template('languages/python/py_setup.html', nav_id="lang-page")

@bp.route('/python/lambda')
def python_lambda():
        return render_template('languages/python/py_lambda.html', nav_id="lang-page")

# ====================================================================
# Subpages of HTML [Programming Languages]
# ====================================================================
@bp.route("/html")
def html():
    return render_template('languages/html/html.html', nav_id="lang-page")

# ====================================================================
# Subpages of CSS [Programming Languages]
# ====================================================================
@bp.route("/css")
def css():
    return render_template('languages/css/css.html', nav_id="lang-page")

# ====================================================================
# Subpages of SQL [Programming Languages]
# ====================================================================
@bp.route("/sql")
def sql():
    return render_template('languages/sql/sql.html', nav_id="lang-page")