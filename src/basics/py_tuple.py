# tuple malumotlar tuzilmasi bolib u ozgarmas (immutable) bolgan elementlar toplamini ifodalaydi
# qiymatlangach unga element qoshish ham ochirish ham imkoni yoq. Listga nisbatan xotira hajmi kamroq va nisbatan
# tezroq. Asosan ozgaras qiymatlar uchun foydalanamiz

# tuple yaratish
t = (1, 2, 3, 4, 5)

# berilgan value qaysi indexda ekanini topib beradi
print(t.index(2))

# value-ning tuple ichida nechta ekanligini aniqlab beradi
print(t.count(2))

# len -> uzunligini topish uchun
print(len(t))

# **** tuple unpacking ****
"""
tuple unpacking bu tuple qiymatlarini bir vaqting ozida ozgaruvchilarga ajratib olish usulidir.
bu usul tuple bilan ishlashni osonlashtiradi va ozgaruvchilarni qiymatlashni osonlashtiradi
"""
# Tuple yaratamiz
my_tuple = (1, 2, 3)

# Unpacking
a, b, c = my_tuple

print("a - ", a)  # Natija: 1
print("b - ", b)  # Natija: 2
print("c - ", c)  # Natija: 3
# Qolgan elementlarni yig‘ib olish (* operatori)
a, *b = my_tuple
print(a, "qolgan elementlari :", b)

students = [("Ali", 25), ("Bobur", 22), ("Lola", 24)]

for name, age in students:
    print(f"student name - {name},student age : {age}")

# zip() bir nechta iteratsiya obyektlarini birlashtiradi va unpack qilish imkonini beradi.
l = [10,20,30]
s = ["Alijon","Diyor","Sardor"]

for name,age in zip(s,l):
    print(f"student name - {name},student age : {age}")

# unpacking orqali join qilish yoki birlashtirish desak ham boladi.
tuple_one = (100,200,300)
tuple_two = (400,500,600)

res = (*tuple_one,*tuple_two)
print("result -> {}".format(res))












