ls = [10, 2, 3, 4, 5, 6]

# oxirgi elementni ochiradi va qiymat qaytaradi
print(ls.pop())

# mavjud listni copy(nusxasini) qaytaradi
print(ls.copy())

# biror elementni listda nechta ekanligini hisoblab beradi
print(ls.count(2))

# listni sortlash uchun ishlatiladi
ls.sort()  # qiymat qaytarmaydi -> none!
print(ls)

# element listning qaysi indexida joylashgan aniqlaydi
print(ls.index(10))

# qiymat ochirish elementga kora
ls.remove(2)
print(ls)

# listni tozalash
ls.clear()
print(ls)

# listga element qoshish
ls.append(10)
ls.append(12)
print(ls)

# listga collection qoshish[1,2]
ls.extend([100, 100])
print(ls)

# listni teskari qilish
ls.reverse()
print(ls)
# yoki
print(ls[::-1])
