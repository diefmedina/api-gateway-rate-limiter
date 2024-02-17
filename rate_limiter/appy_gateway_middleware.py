from flask import Flask, request, jsonify
from .rate_limiter import RateLimiter
from .jwt_handler import JWTHandler

app = Flask(__name__)
redis_manager = RedisManager()

@app.before_request
def before_request():
    jwt_token = request.headers.get('Authorization', '').split('Bearer ')[-1]
    user_id = JWTHandler.extract_user_id(jwt_token)

    if user_id:
        rate_limiter = RateLimiter(user_id, redis_manager)
        if not rate_limiter.is_allowed():
            return jsonify({"error": "Rate limit exceeded. Try again later."}), 429
