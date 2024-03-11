# Creating a blueprint for useful tools
from flask import Blueprint
bp = Blueprint('useful_tools', __name__)
from app.useful_tools import routes