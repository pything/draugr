import logging


class ContextFilterWorstLevel(logging.Filter):
    def __init__(self):
        self.worst_level = logging.INFO

    def filter(self, record):
        if record.levelno > self.worst_level:
            self.worst_level = record.levelno
        return True


# Create a logger object and add the filter
logger = logging.getLogger()
logger.addFilter(ContextFilterWorstLevel())

# Check the worst log level called later
for filter in logger.filters:
    if isinstance(filter, ContextFilterWorstLevel):
        print(filter.worst_level)
