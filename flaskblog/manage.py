import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_script import Manager, Server
from flaskblog import (app, config)

manager = Manager(app)
manager.add_command("runserver", 
                    Server(use_debugger=config.debugger,
                           use_reloader=config.reloader,
                           host=config.host))

if __name__ == '__main__':
    manager.run()