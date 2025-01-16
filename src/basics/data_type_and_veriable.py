"""
O'zgaruvchi – bu ma'lumotlarni vaqtinchalik saqlash uchun nomlangan xotira maydoni. Python tilida o'zgaruvchilarni
oldindan e'lon qilish shart emas, ular to'g'ridan-to'g'ri ishlatiladi.
"""
# ozgaruvchi elon qilish doimgidek qoida hamma dasturlash tilidagi kabi!
x = 10  # Butun son (integer)
y = 5.5  # O'nlik son (float)
name = "Aziz"  # Qator (string)
is_valid = True  # Mantiqiy qiymat (boolean)
# Ma'lumot turi – bu o‘zgaruvchining saqlayotgan qiymatini tavsiflash uchun ishlatiladi. Python’da har bir
# o‘zgaruvchi o‘zining ma'lumot turiga ega. Python avtomatik ravishda ma'lumot turini aniqlaydi, ammo ba'zan
# bu tur o‘zgarishi mumkin

# * Primitive Data Types(int,float,complex,bool,str,none)
# * Non-Primitive Data Types(List,Set,Tuple,Dictionary)


# Primativ turlar
# 1. Integer
age = 25
print(f"Yosh: {age}, turi: {type(age)}")

# 2. Float
height = 5.9
print(f"Bo'y: {height}, turi: {type(height)}")

# 3. Complex
z = 3 + 4j
print(f"Kompleks son: {z}, Haqiqiy qismi: {z.real}, Mavhum qismi: {z.imag}, turi: {type(z)}")

# 4. Boolean
is_active = True
print(f"Aktivmi: {is_active}, turi: {type(is_active)}")

# 5. String
name1 = "Aziz"
greeting = f"Salom, {name1}!"
print(f"Qator: {greeting}, turi: {type(greeting)}")

# 6. NoneType
unknown = None
print(f"Qiymat: {unknown}, turi: {type(unknown)}")

# Non-Primativ turlar
# 7. List
fruits = ["olma", "banan", "anjir", "nok"]
print(f"Ro'yxat: {fruits}, turi: {type(fruits)}")

# 8. Tuple
colors = ("qizil", "yashil", "ko'k")
print(f"Tuple: {colors}, turi: {type(colors)}")

# 9. Set
unique_numbers = {1, 2, 3, 4, 5, 5}  # Takrorlanishlar avtomatik olib tashlanadi
unique_numbers.add(6)  # Yangi element qo'shish
print(f"To'plam: {unique_numbers}, turi: {type(unique_numbers)}")

# 10. FrozenSet
frozen_set = frozenset([1, 2, 3])
print(f"Muzlatilgan To'plam: {frozen_set}, turi: {type(frozen_set)}")

# 11. Dictionary
student = {"name": "Aziz", "age": 25, "subjects": ["Python", "Mathematics"], "grade": "A"}
print(f"Lug'at: {student}, turi: {type(student)}")

# 12. Bytes va Bytearray
byte_data = b"Salom"
byte_array_data = bytearray(b"Python")
byte_array_data[0] = 80  # O'zgartirish faqat bytearray uchun mumkin
print(f"Bytes: {byte_data}, turi: {type(byte_data)}")
print(f"Bytearray: {byte_array_data}, turi: {type(byte_array_data)}")
