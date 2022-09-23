#!/bin/bash
./pybin/bin/python3 ./server.py --env "dev" &
echo $! >sanic.pid
./pybin/bin/python3 ./check_running.py
