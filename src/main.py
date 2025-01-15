from utils.helper import create_directory, read_file, write_file
from utils.logger import setup_logger

# Loggerni sozlash
logger = setup_logger("logs/app.log")

if __name__ == "__main__":
    # Katalog yaratish
    directory_path = "example_folder"
    create_directory(directory_path)
    logger.info(f"Katalog yaratildi: {directory_path}")

    # Faylga yozish
    file_path = f"{directory_path}/example.txt"
    content = "Bu faylga yozilgan matn."
    write_file(file_path, content)
    logger.info(f"Faylga yozildi: {file_path}")

    # Faylni o'qish
    data = read_file(file_path)
    if data:
        logger.info(f"Fayldan o'qildi: {data}")
    else:
        logger.error("Faylni o'qishda xatolik yuz berdi.")
