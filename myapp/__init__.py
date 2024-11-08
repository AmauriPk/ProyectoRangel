from flask import Flask

from myapp.config import DevConfig
from myapp.task.controllers import taskRoute

app = Flask(__name__)
app.register_blueprint(taskRoute)

#app.debug = True
app.config.from_object(DevConfig)


@app.route('/')# esta es la ruta mas global de nuestro proyecto
def hello_world() -> str:
    return ' Hello world'