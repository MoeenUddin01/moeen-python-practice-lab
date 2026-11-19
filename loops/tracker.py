class ApiUsageTracker:
    def __init__(self, daily_limit):
        if (
            isinstance(daily_limit, bool)
            or not isinstance(daily_limit, int)
            or daily_limit <= 0
        ):
            raise ValueError("daily limits must be positive integers")

        self.daily_limits = daily_limit
        self.tokens_used = 0
        self.request_count = 0

    def record_request(self, tokens):
        if isinstance(tokens, bool) or not isinstance(tokens, int) or tokens < 0:
            raise ValueError("tokesn must be a non-negative integer")

        if self.tokens_used + tokens > self.daily_limits:
            raise ValueError("Daily tokesn limits exceeded")

        self.tokens_used += tokens
        self.request_count += 1
        return self.daily_limits - self.tokens_used


if __name__ == "__main__":
    tracker = ApiUsageTracker(2000)
    print(tracker)
    remaining = tracker.record_request(400)
    print(remaining)
