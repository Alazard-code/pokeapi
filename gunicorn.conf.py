import os
from multiprocessing import cpu_count

bind = "0.0.0.0:{}".format(os.environ.get("SERVER_PORT", "80"))
# Worker Settings
workers = 2  # Number of worker processes
threads = 2  # Number of threads per worker
worker_class = 'gthread'  # Use threads instead of processes
max_requests = 1000  # Restart workers after handling this many requests
max_requests_jitter = 50  # Add randomness to max_requests

# Memory Optimization
worker_tmp_dir = '/dev/shm'  # Use RAM-based tmp directory
preload_app = False  # Load app after forking workers