# qiymatlarni key : value korinishida saqlab beradi. duplicat key saqlab bolmaydi

thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)

# murojat qilish :
print(thisdict["name"])

# nusxasini qaytaradi
copy_dict = thisdict.copy()
print(copy_dict)

# Kalitga mos qiymatni olish. Agar qiymat mavjud bolmasa none qaytaradi yoki defould qiymat bersak boladi
person = {"name": "Alice", "age": 25}
print(person.get("name"))  # Alice
print(person.get("gender"))  # Noma'lum

