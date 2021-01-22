#!/bin/bash
# Author: Cloud11665
# ----------------------------
echo "starting python"
echo "restarting web server at port 5000"
#sudo systemctl restart nginx
nohup gunicorn --bind 127.0.0.1:5000 wsgi:app </dev/null >/dev/null 2>&1&
echo "done!"
