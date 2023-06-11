import logging
import os.path
import sys

parent_directory_name = os.path.basename(
    os.path.dirname(
        os.path.realpath(__file__)
    )
)
logger = logging.Logger(name=parent_directory_name)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
logger.addHandler(hdlr=handler)
