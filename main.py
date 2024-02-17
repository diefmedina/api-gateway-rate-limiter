# main.py
from flask import Flask

app = Flask(__name__)

# Import your middleware and other necessary components
from rate_limiter.api_gateway_middleware import before_request
from rate_limiter.config.settings import REQUESTS_PER_MINUTE

# Set up your middleware
app.before_request(before_request)

# Define a test route for demonstration purposes
@app.route('/healthcheck')
def test_route():
    return "Hello, Rate Limiter!"

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
