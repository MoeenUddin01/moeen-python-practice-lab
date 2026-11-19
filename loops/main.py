# run_tracker.py
from tracker import ApiUsageTracker


def main():
    tracker = ApiUsageTracker(500)
    for batch in [200, 250, 100]:
        try:
            left = tracker.record_request(batch)
            print(f"Accepted {batch} tokens | Remaining: {left}")
        except ValueError as err:
            print(f"Rejected {batch} tokens | Reason: {err}")


if __name__ == "__main__":
    main()
