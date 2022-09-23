from importlib import import_module
from sanic import Sanic
import os

basedir = os.path.dirname((os.path.dirname(os.path.dirname(__file__))))
bp_path = os.path.join(basedir, "bp")

print(bp_path)


def load_blueprints(app: Sanic):
    for _, dirs, _ in os.walk(bp_path):
        for d in dirs:
            try:
                if d == "__pycache__":
                    continue
                module = f'bp.{d}.views'
                views = import_module(module)
                print("loading blueprint", module)
                app.blueprint(views.bp)
                print("loaded blueprint", module)
            except ModuleNotFoundError:
                pass
        # only run the loop once
        break
