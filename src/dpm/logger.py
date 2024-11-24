import logging


def configure_logger(logger: logging.Logger, log_file="app.log", level=logging.DEBUG):
    """
    Configure logger
    Logs are written to the specified log file and the console.
    """
    # Define a common format for all log messages
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    # File handler for logging to a file
    file_handler = logging.FileHandler(log_file, mode="a")  # Append to the log file
    file_handler.setLevel(logging.DEBUG)  # Log everything to the file
    file_handler.setFormatter(formatter)

    # Console handler for logging to stdout
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # Only log INFO and above to the console

    # Add handlers to the logger
    if not logger.handlers:  # Avoid duplicate handlers during imports
        logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    # Optional: Customize specific package's logging level
    logger.setLevel(level)


def read_and_log_txt_file(logger, file_path):
    try:
        with open(file_path) as file:
            content = file.readlines()
            for line in content:
                logger.info(f"{line.strip()}")
            return content
    except FileNotFoundError:
        logger.error(f"File {file_path} not found.")
        return None


# Configure logger for dpm
logger = logging.getLogger("dpm")
level = logging.DEBUG
log_file = "logs/dpm.log"
configure_logger(logger, log_file, level)
