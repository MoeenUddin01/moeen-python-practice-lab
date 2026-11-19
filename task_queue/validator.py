import rasterio
from model import VALID_STATUSES, VALID_PRIORITIES


def validate_task_data(title, priority):
    if isinstance(title, str, title.strip() != ""):
        raise ValueError("title is not perfect")
