"""
Spans. Logfire instrument.
"""

from datetime import datetime

import logfire

service_name = "date_announcer_logfire"
logfire.configure(service_name=service_name)

worshop_info = {
    "day": "Thursday",
    "time": "12:00",
    "location": "Online",
    "link": "https://example.com",
    "duration": "1 hour",
    "participants": "Anyone interested in logging and observability",
}


def main():
    with logfire.span("main"):
        """Calculate the current date and weekday and announce the workshop."""
        logfire.info("Initiate function")

        current_date = datetime.now()
        logfire.info("Current date: {current_date}", current_date=current_date)

        if current_date.weekday() == 3:
            print("Today is Thursday, which means it's time for the workshop!")
            logfire.info(
                "Workshop information: {workshop_info}", workshop_info=worshop_info
            )
        else:
            logfire.error("Today is not Thursday, so no workshop today.")
        logfire.info("End function, workshop date has been announced.")


if __name__ == "__main__":
    main()
