import logfire

# service_name
logfire.configure()

logfire.trace("This is a trace message")
logfire.debug("This is a debug message")
logfire.info("This is an info message")
logfire.notice("This is a notice message")
logfire.warn("This is a warning message")
logfire.error("This is an error message")
logfire.fatal("This is a fatal message")
