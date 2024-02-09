#!/bin/sh
gunicorn --chdir src --bind 0.0.0.0:5001 wsgi:app