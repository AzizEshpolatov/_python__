"""
Python'da modul bu — oldindan yozilgan yoki foydalanuvchi tomonidan yaratilgan Python kodlarini o‘z ichiga
oluvchi fayl bo‘lib, bu kodlar boshqa Python dasturlarida qayta ishlatilishi uchun mo‘ljallangan.
Modulni oddiy qilib aytganda, funksiyalar, sinflar va o‘zgaruvchilar to‘plami bo‘lgan fayl sifatida
tasavvur qilish mumkin. Modulni import qilish orqali undagi barcha funksiyalarni va sinflarni ishlatishingiz mumkin.
"""
from function_py import quadratic_roots

if __name__ == "__main__":
    print(quadratic_roots(1, -3, 2))
    print(quadratic_roots(1, 2, 5))

if __name__ == "__main__":
    print(quadratic_roots(1, -3, 2))
    print(quadratic_roots(1, 2, 5))
