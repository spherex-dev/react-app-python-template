###############################################################################
# Copyright (C) 2022, created on February 12, 2022
# Written by Justin Ho
#
# This source code is proprietary and without warranty.
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# Implementation is inspired from https://sanic.dev/en/guide/how-to/cors.html#cors.py
###############################################################################


from typing import Iterable


def _add_cors_headers(response, methods: Iterable[str]) -> None:
    allow_methods = list(set(methods))
    if "OPTIONS" not in allow_methods:
        allow_methods.append("OPTIONS")
    headers = {
        "Access-Control-Allow-Methods": ",".join(allow_methods),
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": "true",
        "Access-Control-Allow-Headers": (
            "origin, content-type, accept, "
            "authorization, x-xsrf-token, x-request-id, "
            "access_token, access_token_signature"
        ),
    }
    response.headers.extend(headers)


def add_cors_headers(request, response):
    if request.method != "OPTIONS":
        methods = [method for method in request.route.methods]
        _add_cors_headers(response, methods)
