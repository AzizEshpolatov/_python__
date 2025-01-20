"""
Positional or Required Arguments
Keyword Arguments
Default Arguments
Positional-only Arguments
Keyword-only arguments
Arbitrary or Variable-length Arguments
"""
# ******************************************************************************************************************** #
# positional or required arguments
"""
Bu argumentlar funksiya chaqirilganda aniq tartibda berilishi kerak. Ular majburiy bo‘lib, agar qiymat uzatilmasa, 
xatolik yuzaga keladi.
"""


def multiply(a, b):
    """Ikki sonni ko'paytirish"""
    return a * b


print(multiply(3, 4))  # Natija: 12
# print(multiply(3))
# Xatolik: missing 1 required positional argument: 'b'

# ******************************************************************************************************************** #
# Keyword Arguments
"""
Bu argumentlar funksiyaga chaqirilganda nomlari bilan uzatiladi. Bu holda, tartib muhim emas, chunki Python kalit 
so‘z asosida qiymatlarni bog‘laydi.
"""


def greet(name, age):
    """Ism va yosh bilan salomlashish."""
    return f"Salom, mening ismim {name}, yoshim {age}!"


# Tartib muhim emas:
print(greet(age=25, name="Ali"))  # Natija: Salom, mening ismim Ali, yoshim 25!

# ******************************************************************************************************************** #
# Default Arguments
"""
Agar argument qiymati berilmasa, standart (default) qiymatdan foydalanadi. Ushbu qiymatlar funksiyani chaqirish vaqtida 
kerakli bo‘lmagan argumentlar uchun ishlatiladi.
"""


def introduce(name, country="O‘zbekiston"):
    """Foydalanuvchini tanishtirish."""
    return f"Men {name}, {country}danman."


print(introduce("Ali"))  # Natija: Men Ali, O‘zbekistondanman.
print(introduce("Karim", "AQSH"))  # Natija: Men Karim, AQSHdanman.
# ******************************************************************************************************************** #
#  Positional-only Arguments
"""
Funksiya faqat tartib asosida qiymat oladigan argumentlar bilan ishlaydi. Bularni kalit so‘z (keyword) sifatida uzatish 
xatolik keltirib chiqaradi. Python 3.8+ versiyalarida qo‘llab-quvvatlanadi.
"""


def add(a, b, /, c):
    """Faqat a va b tartib bilan uzatilishi kerak."""
    return a + b + c


print(add(1, 2, c=3))  # Natija: 6
# print(add(a=1, b=2, c=3))  # Xatolik: Positional-only argument 'a' passed as keyword argument.
# ******************************************************************************************************************** #
# Keyword-only Arguments
"""
Bu argumentlar faqat kalit so‘z sifatida uzatilishi mumkin. Funksiya ichida * ishlatib, buni belgilash mumkin.
"""


def divide(a, b, *, precision=2):
    """A va B bo‘linishi. Precision faqat keyword bilan ishlatiladi."""
    return round(a / b, precision)


print(divide(10, 3, precision=4))  # Natija: 3.3333
# print(divide(10, 3, 4))          # Xatolik: takes 2 positional arguments but 3 were given
# ******************************************************************************************************************** #
# Arbitrary yoki Variable-length Arguments

"""
Funksiya har qanday uzunlikdagi argumentlarni qabul qilishi uchun ishlatiladi. Bu uchun *args (pozitsion argumentlar) 
yoki **kwargs (kalit-so‘z argumentlari) dan foydalaniladi.
"""


def total_sum(*args):
    """Istalgancha sonlarni yig‘ish."""
    return sum(args)


print(total_sum(1, 2, 3, 4))  # Natija: 10
# ******************************************************************************************************************** #
