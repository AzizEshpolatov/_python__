# example
text = "  Python is awesome! It is used for Web, AI, Data Science, and more. "
"""
Matn boshidagi va oxiridagi ortiqcha bo‘sh joylarni olib tashlang.
Matndagi barcha so‘zlarni kichik harflarga o‘tkazing.
Matndagi har bir is so‘zini IS bilan almashtiring.
, bilan ajratilgan so‘zlarni alohida ro‘yxatga o‘tkazing.
Matndagi barcha so‘zlarning sonini hisoblang.
Barcha so‘zlarni alifbo tartibida joylashtiring va - bilan birlashtirib, bitta string qaytaring.
"""
words = text.strip().lower().replace("is", "IS").split(",")
result_length = len(" ".join(words).split())
result_words = "-".join(sorted(words))

print("sozning uzunligi : {}".format(result_length))
print("natija : {}".format(result_words))

"""  ----------------  string method --------------------------"""
s = "hello world!!!"

# upper()
print(s.upper())  # hammasini katta harfga aylantiradi.

# lower()
print(s.lower())  # hammasini kichikka aylantiradi

# title
print(s.title())  # har bir sozning bosh harfini katta qilib beradi.

# capitalize() faqat birinchi harfini katta qilib beradi
print(s.capitalize())

# swapcase()
print(s.swapcase())  # Katta harflarni kichik, kichik harflarni katta qiladi.

# strip()
print(s.strip())  # Boshi va oxiridagi bo‘sh joylarni olib tashlaydi.

# lStrip() and rStrip()
print(s.lstrip())  # boshidagi yoki(rStrip) oxiridagi bosh joylarni olib tashlaydi

# center(width)
print(s.center(100))  # berilgan width boyicha centr qiladi

# (l,r)just(with)
print(s.ljust(10))  # matnni chapga tekislaydi
print(s.rjust(10))  # matnni o'ngga tekislaydi

# find(sub)
print(s.find("ll"))  # matnni ichidan berilgan qiiymatning indexini qaytaradi topilmasa -1

# rfind(sub)
print(s.rfind("o"))  # matnning oxiridan qidiradi

# index(sub) -> findga o'xshash agar topolmasa error beradi
# rindex(sub) rfind(sub)-ga o'xshash.

# replace() -> almashitirsh.
print(s.replace("hello", "HELLOO!!!! "))

# str.zfill(width)
print("23".zfill(10))  # sonlarning(soz bolsa ham) oldiga 0 qoyib beradi

# (starts,ends)with(sub)
print(s.startswith("!!!!"))  # Berilgan qator bilan boshlansa(tugasa) True, aks holda False

# isalpha
print(s.isalpha())  # faqat harflardan iborat bolsa true aks holda false!

# isDigit
print(s.isdigit())  # faqat raqamlardan iborat bolsa true aks holda false

# isalnum
print(s.isalnum())  # harf va raqamlardan iborat bolsa true aks holda false

# isspace
print(s.isspace())  # bosh joylardan iborat bolsa true aks holda false

# islower
print(s.islower())  # hammasi kichik bolsa true aks holda false

# isupper
print(s.isupper())  # hammasi katta bolda true aks holda false

# casefold
print("ß".casefold())  # Katta harflarni kichikka o‘tkazadi, lekin lower()dan kuchliroq. ß -> maxsus iishlanadi : "ss"

# expandtabs
print("A\tB\tC".expandtabs(3))  # stringdagi \t (tab) belgisini berilgan bo‘shliq miqdoriga kengaytiradi.

# format_map
data = {"name": "Ali", "age": 20}
template = "my name is {name} and I am age {age} years old"
print(template.format_map(data))  # berilgan lug‘dictionaryni qiymatlarni o‘z o‘rniga qo‘yadi.

# .join()
print(",".join(['a', 'b', 'c', 'd']))  # 1ta stringga yigib beradi

# partition
print(s.partition(" "))  # Matnni berilgan ajratuvchi (sep) bo‘yicha uch qismga bo‘ladi

# splitlines()
print(s.splitlines())  # Matnni qator bo‘yicha (\n) bo‘ladi

# maketrans (Matn ichidagi belgilarning xaritasiga ko‘ra o‘zgartirish amalga oshiradi.)
trans = str.maketrans("aeiou", "12345")  # 'a' -> '1', 'e' -> '2'
print(trans)

table = str.maketrans("abc", "123", "d")
print("abcdabc".translate(table))  # 123123 (d olib tashlandi)

print(234)