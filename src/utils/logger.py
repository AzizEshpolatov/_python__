# utils/logger.py

import logging
import os


def setup_logger(log_file="app.log"):
    """
    Loggerni sozlash funksiyasi.
    Loglarni faylga va konsolga yozadi.
    """
    # Log fayli uchun katalog yaratish
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Loggerni sozlash
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),  # Faylga log yozish
            logging.StreamHandler()  # Konsolga log yozish
        ]
    )
    logger = logging.getLogger()
    return logger
