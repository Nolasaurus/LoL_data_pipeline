import time

class RateLimiter:
    def __init__(self, max_requests, period):
        self.max_requests = max_requests
        self.period = period
        self.timestamps = []

    def __call__(self):
        now = time.time()
        self.timestamps = [ts for ts in self.timestamps if ts > now - self.period]

        if len(self.timestamps) < self.max_requests:
            self.timestamps.append(now)
        else:
            oldest_request = min(self.timestamps)
            time_to_wait = self.period - (now - oldest_request)
            time.sleep(time_to_wait)
            self.timestamps.append(time.time())

rl_sec = RateLimiter(20, 1)  # 20 requests per 1 second
rl_min = RateLimiter(100, 120)  # 100 requests per 2 minutes