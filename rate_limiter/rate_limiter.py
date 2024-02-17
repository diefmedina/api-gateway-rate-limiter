from datetime import datetime, timedelta
from .redis_manager import RedisManager
from .config.settings import REQUESTS_PER_MINUTE

class RateLimiter:
    def __init__(self, user_id, redis_manager=None):
        self.user_id = user_id
        self.redis_manager = redis_manager or RedisManager()
        self.window_size = 60  # 1 minute window

    def is_allowed(self):
        key = f"rate_limiter:{self.user_id}"
        current_counter = self.redis_manager.get_counter_value(key)

        if current_counter < REQUESTS_PER_MINUTE:
            self.redis_manager.set_counter_value(key, current_counter + 1, self.window_size)
            return True
        else:
            return False
