@echo off
set FLASK_APP=src
set FLASK_ENV=production
set FLASK_RUN_PORT=5000
flask run --host=0.0.0.0
