from flask import render_template
from app.data_structures import bp

# Routes for pages associated with data structures

@bp.route('/')
def index():
    return render_template('data_structures.html', nav_id="struct-page")

# ====================================================================
# Subpages of Data Structures
# ====================================================================

@bp.route('/arrays')
def arrays():
    return render_template('data_structures/linear/arrays.html', nav_id="struct-page")

@bp.route('/linked_lists')
def linked_lists():
    return render_template('data_structures/linear/linked_lists.html', nav_id="struct-page")

@bp.route('/queues')
def queues():
    return render_template('data_structures/linear/queues.html', nav_id="struct-page")

@bp.route('/stacks')
def stacks():
    return render_template('data_structures/linear/stacks.html', nav_id="struct-page")

@bp.route('/hash_tables')
def hash_tables():
    return render_template('data_structures/linear/hash_tables.html', nav_id="struct-page")