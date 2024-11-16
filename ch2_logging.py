from datetime import datetime
from logging import INFO, basicConfig, getLogger

import logfire

service_name = "date_announcer"
logfire.configure(service_name=service_name)

basicConfig(level=INFO, handlers=[logfire.LogfireLoggingHandler()])

logger = getLogger(__name__)


def main():
    """Calculate the current date and weekday and announce the workshop."""
    logger.info("Initiate function")

    current_date = datetime.now()
    logger.info(f"Current date: {current_date}")
    if current_date.weekday() == 3:
        print("Today is Thursday, which means it's time for the workshop!")
    else:
        print("Today is not Thursday, so no workshop today.")
    logger.info("End function, workshop date has been announced.")


if __name__ == "__main__":
    main()
