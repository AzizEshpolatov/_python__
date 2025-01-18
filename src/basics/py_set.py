"""
Set ichida bir xil qiymatli elementlar bo‘lmaydi. Agar setga takroriy elementlar qo‘shilsa, u avtomatik
ravishda faqat bir marta saqlanadi.
Setlar ichidagi elementlar tartiblanmagan (unordered), shuning uchun ularni indeks orqali chaqirib bo‘lmaydi.
Setga yangi elementlar qo‘shish yoki mavjudlarini o‘chirish mumkin, lekin elementlar o‘zlari o‘zgarmas (immutable)
bo‘lishi kerak.Faqat unikal qiymatlar saqlanadi.
"""

my_set = set()
print(my_set)  # Natija: set()

fruits = {"olma", "banan", "apelsin"}
print(fruits)  # Natija: {'olma', 'banan', 'apelsin'}

# consolga chiqarish
for fruit in fruits:
    print(fruit)

# bir qancha element qoshish
fruits.update(["shaftoli", "uzum"])
print(fruits)  # Natija: {'olma', 'uzum', 'shaftoli', 'banan', 'apelsin'}

# element o'chirish
fruits.remove("banan")
print(fruits)  # Natija: {'olma', 'apelsin'}

# tasodifiy birorta elementini ochirish
removed_item = fruits.pop()
print(removed_item)  # Tasodifiy element
print(fruits)  # Qolgan elementlar

# 2ta set birlashmasi
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
print(union_set)  # Natija: {1, 2, 3, 4, 5}

# kesishmasi
intersection_set = set1.intersection(set2)
print(intersection_set)  # natija : {3}

# Difference -> bu method orqali faqat 1-setdagi(2-setda mavjud bolmagan) elementlarini qaytaradi
res = set1.difference(set2)
print(res)

# symmetric_difference -> ikkisida ham mavjud bolmagan elementlarni qaytaradi.
symmetric_diff = set1.symmetric_difference(set2)
print(symmetric_diff)  # Natija: {1, 2, 4, 5}
