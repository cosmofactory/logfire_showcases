import logfire

logfire.configure(service_name="entrypoint", inspect_arguments=True)
logfire.install_auto_tracing(modules=["ch4_instrument_1"], min_duration=0)

from ch4_instrument_1 import main  # noqa

main()
