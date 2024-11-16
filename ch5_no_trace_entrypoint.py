import logfire

logfire.configure(service_name="no_trace")
logfire.install_auto_tracing(modules=["ch5_no_trace"], min_duration=0)

from ch5_no_trace import main  # noqa

main()
