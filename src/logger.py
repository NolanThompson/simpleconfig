import logging

def setup_logger(log_file):
    logger = logging.getLogger("iptables_translator")
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(message)s")
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

def log_event(logger, user_input, iptables_command):
    logger.info(f"User input: {user_input}")
    logger.info(f"Iptables command executed: {iptables_command}")