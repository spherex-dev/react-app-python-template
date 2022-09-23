from argparse import ArgumentParser

from sanic import Sanic

from utils.bp import load_blueprints
from utils.cors import setup_cors

app = Sanic("main")


def setup(app, env):

    if env == "dev":
        # warning, we setup CORS to allow access from any host
        # do not your website with env = "dev" as this may pose
        # a security risk, it is best to put a reverse proxy
        # such as nginx in front and route /api/* to this service
        # instead.
        setup_cors(app)
    load_blueprints(app)


if __name__ == "__main__":
    p = ArgumentParser(description="Argument parsing to start server")
    p.add_argument("--port", type=int, default=8000)
    p.add_argument("--env", type=str, default="prod")

    args = p.parse_args()

    setup(app, args.env)
    auto_reload = args.env != "prod"
    app.run(port=args.port, motd=False)
