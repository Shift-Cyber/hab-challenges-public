#!/bin/bash
python3 -m gunicorn -k flask_sockets.worker server:app -w 4 -b 0.0.0.0:80 --log-level INFO
