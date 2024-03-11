from flask import render_template
from app.languages import bp

# Routes for pages associated with data structures

@bp.route("/languages")
def languages():
    return render_template('languages.html', nav_id="lang-page")

# ====================================================================
# Subpages of C [Programming Languages]
# ====================================================================

# Accessing C Main Page
@bp.route("/c")
def c():
    return render_template('languages/c/c.html', nav_id="lang-page")

@bp.route('/c/<path:pagename>')
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
@bp.route("/cpp")
def cpp():
    return render_template('languages/cpp/cpp.html', nav_id="lang-page")

@bp.route('/cpp/<path:pagename>')
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
@bp.route("/cs")
def cs():
    return render_template('languages/cs/cs.html', nav_id="lang-page")

@bp.route('/cs/<path:pagename>')
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
@bp.route("/java")
def java():
    return render_template('languages/java/java.html', nav_id="lang-page")

@bp.route('/java/<path:pagename>')
def java_route(pagename):
    if pagename == 'Main':
        return render_template('languages/java/java.html', nav_id="lang-page")
    else:
        return render_template('404.html', nav_id="lang-page")

# ====================================================================
# Subpages of JavaScript [Programming Languages]
# ====================================================================

# Accessing JavaScript Main Page
@bp.route("/javascript")
def javascript():
    return render_template('languages/javascript/javascript.html', nav_id="lang-page")

@bp.route('/javascript/<path:pagename>')
def javascript_route(pagename):
    if pagename == 'Main':
        return render_template('languages/javascript/javascript.html', nav_id="lang-page")
    else:
        return render_template('404.html', nav_id="lang-page")

# ====================================================================
# Subpages of Python [Programming Languages]
# ====================================================================

# Accessing Python Main Page
@bp.route("/python")
def python():
    return render_template('languages/python/python.html', nav_id="lang-page")

@bp.route('/python/<path:pagename>')
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
@bp.route("/html")
def html():
    return render_template('languages/html/html.html', nav_id="lang-page")

@bp.route('/html/<path:pagename>')
def html_route(pagename):
    if pagename == 'Main':
        return render_template('languages/html/html.html', nav_id="lang-page")
    else:
        return render_template('404.html', nav_id="lang-page")

# ====================================================================
# Subpages of CSS [Programming Languages]
# ====================================================================

# Accessing CSS Main Page
@bp.route("/css")
def css():
    return render_template('languages/css/css.html', nav_id="lang-page")

@bp.route('/css/<path:pagename>')
def css_route(pagename):
    if pagename == 'Main':
        return render_template('languages/css/css.html', nav_id="lang-page")
    else:
        return render_template('404.html', nav_id="lang-page")

# ====================================================================
# Subpages of SQL [Programming Languages]
# ====================================================================

# Accessing SQL Main Page
@bp.route("/sql")
def sql():
    return render_template('languages/sql/sql.html', nav_id="lang-page")

@bp.route('/sql/<path:pagename>')
def sql_route(pagename):
    if pagename == 'Main':
        return render_template('languages/sql/sql.html', nav_id="lang-page")
    else:
        return render_template('404.html', nav_id="lang-page")