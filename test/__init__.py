from pathlib import Path

from .logger_ import logger, read_and_log_txt_file

welcome_file = Path(__file__).parent / "bin" / "welcome.txt"
# TODO: generate automatically welcome file
read_and_log_txt_file(logger, welcome_file)
