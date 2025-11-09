class RateLimiter:
    def __init__(self, n):
        self.n = n
        self.window = []

    def allow_request(self):
        now = time.time()
        # Prune old entries from window
        # (logic hidden)
        # Return True or False based on count
        # (main logic hidden)
