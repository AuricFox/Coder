# Creating a blueprint fordata structures
from flask import Blueprint
bp = Blueprint('data_types', __name__)
from app.data_structures import routes