from flask import render_template
from app.useful_tools import bp

# Routes for pages associated with useful_tools

@bp.route("/useful_tools")
def useful_tools():
    return render_template('useful_tools.html', nav_id="tools-page")

# ====================================================================
# Subpages of Useful Tools 
# ====================================================================