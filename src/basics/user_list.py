"""
UserList collection modulining bir qismi bolib, list obyektini kengaytirish uchun ishlatiladi
U oddiy list kabi ishlaydi ammo hatti harakatlarni moslashitirishimiz mumkin boladi.
UserList -> listning barcha  methodlarini meros qilib oladi. UserList ham oddiy list kabi moslashuvchan boladi
Ma'lumotni kiritishdan oldin tekshirish uchun qulay.
"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newList = [x for x in fruits if "a" in x]
newList = [x.upper() for x in fruits]
print(newList)
