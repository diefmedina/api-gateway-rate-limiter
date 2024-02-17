# api-gateway-rate-limiter
Python Code Challenge  API Gateway Rate Limiter with Fixed Window Counter


### Objective:
Design and implement a rate limiter at the API gateway level using the Fixed Window
Counter algorithm, leveraging Redis for state management. The rate limiter should use
JWT tokens to identify users and apply rate limits accordingly.


### Key Requirements:

* Rate Limiting Logic: Implement the Fixed Window Counter algorithm to enforce rate
limits on API requests. Each user (identified by a unique identifier in the JWT) should have
their own fixed window counter.

* JWT Integration: Extract the user identifier from the JWT payload to apply user-specific
rate limits.

* Redis: Use Redis to store and manage rate limit counters for each user. Ensure counters
reset at the end of each fixed window period.

* Response Handling: When a rate limit is exceeded, the API gateway should return a 429
Too Many Requests status code with a message indicating when the user can try again.

* Configuration: Allow configurable rate limits (e.g., requests per minute). This
configuration could be stored in a single .env file.

### Considerations:
Don&#39;t focus on a functional microservice, but create the structure following best practices,
then implement the rater limit functionality in a single class with unit tests.

### Deliverables:
Share the code in a public GitHub repository, again following best practices.

### Skillset to evaluate:
Python code quality, testing, API design, Redis proficiency, JWT handling, algorithmic
Skills, best practices