from sanic import Blueprint
from sanic.response import json
from sanic.request import Request
bp = Blueprint("hello", url_prefix="api/hello")


@bp.route("hello")
async def hello(request: Request):
    return json({"hello": "world"})


@bp.route("greeting/<greeting>")
async def greeting(request: Request, greeting: str):
    "Example of returning a greeting based on a dynamic get url"
    return json({"greeting": greeting})


@bp.route("echo_post", methods=["POST"])
async def echo_post(request: Request):
    "An echo route that returns the posted data"
    return json(request.json)
