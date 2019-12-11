from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import (Migrate, MigrateCommand)
from database import (db, engine, Base)

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()