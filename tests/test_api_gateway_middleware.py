import unittest
from flask import Flask
from unittest.mock import patch
from rate_limiter.api_gateway_middleware import before_request

class TestApiGatewayMiddleware(unittest.TestCase):
    @patch('rate_limiter.rate_limiter.RateLimiter.is_allowed', return_value=True)
    @patch('rate_limiter.jwt_handler.JWTHandler.extract_user_id', return_value="user123")
    def test_before_request_allowed(self, mock_extract_user_id, mock_is_allowed):
        app = Flask(__name__)
        app.before_request(before_request)

        with app.test_request_context(headers={'Authorization': 'Bearer valid_token'}):
            response = app.preprocess_request()
            self.assertIsNone(response)

    @patch('rate_limiter.rate_limiter.RateLimiter.is_allowed', return_value=False)
    @patch('rate_limiter.jwt_handler.JWTHandler.extract_user_id', return_value="user123")
    def test_before_request_not_allowed(self, mock_extract_user_id, mock_is_allowed):
        app = Flask(__name__)
        app.before_request(before_request)

        with app.test_request_context(headers={'Authorization': 'Bearer valid_token'}):
            response = app.preprocess_request()
            self.assertEqual(response.status_code, 429)
