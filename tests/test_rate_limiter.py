import unittest
from unittest.mock import patch
from rate_limiter.rate_limiter import RateLimiter

class TestRateLimiter(unittest.TestCase):
    @patch('rate_limiter.redis_manager.RedisManager')
    def test_rate_limiter(self, mock_redis_manager):
        rate_limiter = RateLimiter("user123", mock_redis_manager)
        self.assertTrue(rate_limiter.is_allowed())
