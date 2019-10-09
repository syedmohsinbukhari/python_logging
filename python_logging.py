import os
import logging
from logging import info, debug


def setup_logging(log_fname=''):
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    if log_fname != '':
        try:
            if not os.path.exists(log_fname):
                os.mknod(log_fname)

            format_string = "%(asctime)s [%(filename)s:%(lineno)s - " + \
                        "%(funcName)s() ] [%(levelname)s] %(message)s"
            file_handler = logging.FileHandler(f"{log_fname}")
            file_formatter = logging.Formatter(format_string)
            file_handler.setFormatter(file_formatter)
            file_handler.setLevel(logging.DEBUG)
            root_logger.addHandler(file_handler)

        except Exception as e:
            info(e)

    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter(
        "[%(levelname)s] - [%(filename)s:%(lineno)s] - %(message)s"
    )
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(logging.INFO)
    root_logger.addHandler(console_handler)


if __name__ == '__main__':
    setup_logging('./python_logging.log')
    print("Hello World")
    info("This is Info")
    debug("This is Debug")
