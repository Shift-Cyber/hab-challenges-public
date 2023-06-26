#!/bin/bash
python3 -m gunicorn server:app -w 4 -b 0.0.0.0:80 --log-level INFO
