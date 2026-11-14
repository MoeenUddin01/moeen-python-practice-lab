# main.py
from config import APP_NAME, VERSION
from loggers import setup_loggers
from text_processer import TextProcessor

logger = setup_loggers("MainApp")


def main():
    logger.info(f"Starting {APP_NAME} (v{VERSION})")

    # Sample raw text payload (simulating incoming data)
    raw_input = (
        "   Hello AI Engineer!     Modular coding makes codebases   bulletproof.   "
    )

    try:
        # Initialize our processor
        processor = TextProcessor()

        # Run pipeline steps
        cleaned = processor.clean_text(raw_input)
        tokens = processor.estimate_tokens(raw_input)

        print("\n--- Pipeline Results ---")
        print(f"Cleaned Text: '{cleaned}'")
        print(f"Token Estimate: {tokens} tokens")

        logger.info("Pipeline executed successfully.")

    except Exception as e:
        logger.critical(f"Pipeline failed with error: {e}")


if __name__ == "__main__":
    main()
