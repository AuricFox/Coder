from flask import render_template
from app.data_structures import bp

# Routes for pages associated with data structures

@bp.route('/')
def index():
    return render_template('data_structures.html', nav_id="struct-page")

# ====================================================================
# Subpages of Data Structures
# ====================================================================

@bp.route('/<path:pagename>')
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