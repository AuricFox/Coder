from flask import render_template
from app.data_types import bp

# Routes for pages associated with data types

@bp.route('/')
def index():
    return render_template('data_types.html', nav_id="data-page")

# ====================================================================
# Subpages of Data Types
# ====================================================================

@bp.route('/integers')
def integers():
    return render_template('data_types/integers.html', nav_id="data-page")

@bp.route('/floats')
def floats():
    return render_template('data_types/floats.html', nav_id="data-page")

@bp.route('/dates')
def dates():
    return render_template('data_types/dates.html', nav_id="data-page")

@bp.route('/characters')
def characters():
    return render_template('data_types/characters.html', nav_id="data-page")

@bp.route('/strings')
def strings():
    return render_template('data_types/strings.html', nav_id="data-page")

@bp.route('/booleans')
def booleans():
    return render_template('data_types/booleans.html', nav_id="data-page")

@bp.route('/nulls')
def nulls():
    return render_template('data_types/nulls.html', nav_id="data-page")