from flask import render_template
from app.data_types import bp

# Routes for pages associated with data types

@bp.route('/')
def index():
    return render_template('data_types.html', nav_id="data-page")

# ====================================================================
# Subpages of Data Types
# ====================================================================

@bp.route('/<path:pagename>')
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