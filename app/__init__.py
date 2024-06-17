from flask import Flask, render_template
import logging, os

PATH = os.path.dirname(os.path.abspath(__file__))
LOG_FOLDER = os.path.join(PATH, '../logs')
os.makedirs(LOG_FOLDER, exist_ok=True)

# Configure the logging object
logging.basicConfig(
    filename=os.path.join(LOG_FOLDER, 'app.log'),
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s]: %(message)s'
)

LOGGER = logging.getLogger(__name__)

def init_app():
    '''
    Initializes the flask application

    Parameter(s): None

    Output(s):
        app (Object): flask application object
    '''
    app = Flask(__name__, instance_relative_config=False)
    # Configured for development
    app.config.from_object('config.DevConfig')

    # Custom page not found
    def page_not_found(error):
        return render_template('404.html'), 404

    with app.app_context():
        # Import routes and custom modules
        from app.main import bp as main_bp
        from app.data_structures import bp as data_structures_bp
        from app.data_types import bp as data_types_bp
        from app.languages import bp as languages_bp
        from app.useful_tools import bp as useful_tools_bp

        # Register blueprint to link routes
        app.register_blueprint(main_bp)
        app.register_blueprint(data_structures_bp, url_prefix='/data_structures')
        app.register_blueprint(data_types_bp, url_prefix='/data_types')
        app.register_blueprint(languages_bp, url_prefix='/languages')
        app.register_blueprint(useful_tools_bp, url_prefix='/useful_tools')

        app.register_error_handler(404, page_not_found)

    return app