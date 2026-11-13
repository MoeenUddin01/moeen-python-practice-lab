from plaintext import loggers
from loggers import setup_logger


class TextProcessor:

    def __init__(self, max_length=500):
        self.max_length = max_length

    def clean_text(self, raw_text):
        if not isinstance(raw_text, str):
            loggers.error("Invalid input type provided to clean_text")
            raise TypeError("input must be string")

        loggers.info("Cleaning Raw test_input--")
        cleaned = "".join(raw_text.split())
        return cleaned

    def estimate_tokens(self, text):
        cleaned = self.clean_text(text)
        token_count = len(cleaned) // 4
        loggers.info(f"Estimated tokens count :{token_count}")

        return token_count
