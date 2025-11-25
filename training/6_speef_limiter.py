# Implement a simple rate limiter allowing N requests per second.

from collections import deque
import time


class RateLimiter:
    def __init__(self, n):
        self.n = n  # max requests allowed per second
        self.timestamps = deque()

    def allow_request(self):
        current = time.time()
        # Remove timestamps older than 1 second
        while self.timestamps and current - self.timestamps[0] > 1:
            self.timestamps.popleft()

        if len(self.timestamps) < self.n:
            self.timestamps.append(current)
            return True
        else:
            return False


# Example usage:
limiter = RateLimiter(3)  # Allow max 3 requests per second

for i in range(5):
    allowed = limiter.allow_request()
    print(f"Request {i+1} allowed: {allowed}")
    time.sleep(0.3)  # Wait 300ms between requests
