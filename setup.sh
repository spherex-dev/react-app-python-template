#!/bin/bash

yarn install
cd backend
virtualenv pybin
. ./pybin/bin/python3
pip install -r requirements.txt
cd ..