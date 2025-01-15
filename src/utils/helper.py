# utils/helper.py
import os


def create_directory(path):
    """
    Berilgan yo'lda katalog (directory) yaratadi.
    Agar katalog allaqachon mavjud bo'lsa, xatolik bermaydi.
    """
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Katalog yaratildi yoki allaqachon mavjud: {path}")
    except Exception as e:
        print(f"Katalogni yaratishda xatolik: {e}")


def read_file(file_path):
    """
    Fayldan ma'lumotlarni o'qib qaytaradi.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Fayl topilmadi: {file_path}")
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
        return None


def write_file(file_path, content):
    """
    Berilgan faylga ma'lumot yozadi.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Faylga yozildi: {file_path}")
    except Exception as e:
        print(f"Faylga yozishda xatolik: {e}")
