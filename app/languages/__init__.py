# Creating a blueprint for programming languages
from flask import Blueprint
bp = Blueprint('languages', __name__)
from app.languages import routes