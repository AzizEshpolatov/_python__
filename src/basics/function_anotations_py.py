"""
Python'dagi function annotations — bu funksiyalardagi parametrlarga va qaytariladigan qiymatlarga oid ma'lumotlarni
kiritish uchun ishlatiladigan sintaksis. Ular faqat qo'shimcha ma'lumotlar berish uchun mo'ljallangan bo'lib, Python
interpretatori tomonidan bajarilmaydi yoki tekshirilmaydi. Ular asosan kodni tushunarli qilish va statik tahlil yoki
hujjatlash vositalariga yordam berish uchun ishlatiladi.

"""
from typing import List, Dict


def foydalanuvchi_malumotlari(foy: Dict[str, str], dostlar: List[str]) -> str:
    return f"Foydalanuvchi: {foy['ism']} {foy['familiya']}, Do'stlari: {', '.join(dostlar)}"


foy = {"ism": "Tolib", "familiya": "Rakhmonov"}
dostlar = ["Ali", "Vali", "Salim"]
print(foydalanuvchi_malumotlari(foy, dostlar))


def toliq_isim(ism: str, familiya: str) -> str:
    return f"{ism} {familiya}"


print(toliq_isim("Aziz", "Eshpolatov"))


def numbers_sum(a: int, b: int, c: int) -> int:
    return a + b + c


print(numbers_sum(1, 2, 3))


def salom_ber(ism: str, yosh: int) -> str:
    return f"Salom, mening ismim {ism}, yoshim {yosh} da."


print(salom_ber.__annotations__)
