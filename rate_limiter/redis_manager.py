import redis

class RedisManager:
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis_conn = redis.StrictRedis(host=host, port=port, db=db)

    def get_counter_value(self, key):
        return int(self.redis_conn.get(key) or 0)

    def set_counter_value(self, key, value, expiration_seconds):
        self.redis_conn.setex(key, expiration_seconds, value)
