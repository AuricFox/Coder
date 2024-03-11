from flask import Flask

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

    return app