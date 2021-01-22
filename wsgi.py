# coding=utf-8
from main import app

if __name__ == '__main__':
    app.run(processes=2, threaded=False)

# gunicorn --bind 127.0.0.1:5000 wsgi:app
