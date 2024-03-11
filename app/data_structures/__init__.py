# Creating a blueprint from data structures
from flask import Blueprint
bp = Blueprint('data_structures', __name__)
from app.data_structures import routes