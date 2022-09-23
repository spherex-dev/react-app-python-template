#!/bin/bash

yarn install
cd backend
virtualenv pybin
. ./pybin/bin/activate
pip install -r requirements.txt
cd ..