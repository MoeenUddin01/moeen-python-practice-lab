from config import DEFAULT_PRIORITY, VALID_STATUSES, VALID_PRIORITIES


class Task:
    def __init__(
        self,
        task_id,
        title,
        priority=DEFAULT_PRIORITY,
    ):
        self.task_id = task_id
        self.title = title
        self.priority = priority
        self.status = "pending"

    def mark_completed(self):
        self.status = "completed"
        return self.status


if __name__ == "__main__":
    task1 = Task(112, "the kings road")
    print(task1.mark_completed())
