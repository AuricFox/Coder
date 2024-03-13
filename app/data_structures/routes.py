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
    return render_template('data_structures/arrays.html', nav_id="struct-page")

@bp.route('/linked_lists')
def linked_lists():
    return render_template('data_structures/linked_lists.html', nav_id="struct-page")

@bp.route('/queues')
def queues():
    return render_template('data_structures/queues.html', nav_id="struct-page")

@bp.route('/stacks')
def stacks():
    return render_template('data_structures/stacks.html', nav_id="struct-page")

@bp.route('/hash_tables')
def hash_tables():
    return render_template('data_structures/hash_tables.html', nav_id="struct-page")