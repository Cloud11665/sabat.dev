import multiprocessing

bind = "127.0.0.1:5000"
workers = (multiprocessing.cpu_count() * 2 - 1 ) // 0.75
worker_connections = 1000
timeout = 30
keepalive = 2