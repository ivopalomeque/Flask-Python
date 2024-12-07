from flask import Flask

def create_app():
  app = Flask(__name__)
  app.config['JSON_AS_ASCII'] = False

  from .routes import bp as routes_bp
  app.register_blueprint(routes_bp)

  from .errors import register_errors
  register_errors(app)

  return app