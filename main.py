from flask import Flask

app = Flask(__name__)

from rate_limiter.api_gateway_middleware import before_request
from rate_limiter.config.settings import REQUESTS_PER_MINUTE

app.before_request(before_request)

@app.route('/healthcheck')
def test_route():
    return "Hello, Rate Limiter!"

if __name__ == '__main__':
    app.run(debug=True)
