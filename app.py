from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)


@app.route("/")
def index():
    return "Welcome to my DevOps app!"


@app.route("/visit")
def visit():
    try:
        count = r.incr("visits")
        return f"Visit count: {count}"
    except redis.RedisError:
        return "Error connecting to Redis", 500


@app.route("/health")
def health():
    try:
        r.ping()
        return "OK", 200
    except redis.RedisError:
        return "Redis connection failed", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
