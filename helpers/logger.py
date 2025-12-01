from loguru import logger
import os

#log file path
LOG_FILE_PATH = 'tests/test_site.log'

def loguru_setup():
    logger.remove()  #removes old sinks

    if os.path.exists(LOG_FILE_PATH):
        try:
            os.remove(LOG_FILE_PATH)
        except Exception as e:
            print(f"Log file {LOG_FILE_PATH} is not found")

    logger.add(
        LOG_FILE_PATH,
        level='INFO',
        retention='1 week',
        encoding='utf-8'
    )
loguru_setup()
log = logger



