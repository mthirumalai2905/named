"""named - Main entry point."""

import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


def main():
    """Application entry point."""
    logger.info("Starting named")
    logger.info("named initialized successfully")


if __name__ == "__main__":
    main()
