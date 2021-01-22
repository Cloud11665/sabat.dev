from app import app

if __name__ == '__main__':
    app.run(processes=2, threaded=False)