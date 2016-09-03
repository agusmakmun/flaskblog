from flask import Flask
from flask_mongoengine import MongoEngine
from flaskblog import config

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'DB': config.MONGODB_SETTINGS}
app.config['SECRET_KEY'] = config.SECRET_KEY

db = MongoEngine(app)

def register_blueprints(app):
    from flaskblog.views import posts
    from flaskblog.admin import admin

    app.register_blueprint(posts)
    app.register_blueprint(admin)

register_blueprints(app)

if __name__ == '__main__':
    app.run()