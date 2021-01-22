#!/bin/bash
# Author: Cloud11665
# ----------------------------
echo "starting python"
#source "$(find $PWD -name activate)"
echo "restarting web server at port 5000"
#sudo lsof -i:5000 | awk '/python/ {print $2}' | xargs sudo kill -9
#sudo systemctl restart nginx
nohup gunicorn --bind 127.0.0.1:5000 wsgi:app </dev/null >/dev/null 2>&1 &
echo "done!"
