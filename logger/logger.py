import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_operation(operation: str, result: str):
    logging.info(f"Operation: {operation}, Result: {result}")
