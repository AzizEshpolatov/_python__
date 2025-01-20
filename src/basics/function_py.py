# *args and **kwargs
def numbers_sum(*args, **kwargs):
    print("Pozitsional argumentlar:", args)
    print("Kalit-so'z argumentlari:", kwargs)


numbers_sum(1, 2, 3, ism="Ali", yosh=25)


# *args -> funksiyaga koplab positional parametrlar uzatish uchun ishlatiladi.
# args yordamida bir qancha argumentlarni tuple korinishida qabul qilishimiz mumkin.

# *kwars esa key-value argumentlari qabul qilish uchun ishlatiladi.
def salomlashish(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")


# Bu yerda **kwargs kalit-so'z (keyword) argumentlarini qabul qiladi va kwargs.items() orqali ularni boshqaradi.

salomlashish(ism="Ali", yosh=25, shahar="Tashkent")

# lambda
# pythonda lambda nomsiz funksiyalar bolib oddiy function-ga qaraganda qisqaroq yozish imkonini beradi
# lambda arguments: expression
"""
lambda — bu Python'da anonim funktsiya yaratish uchun kalit so'z.
arguments — funktsiyaga uzatiladigan argumentlar (bir yoki bir nechta).
expression — bu argumentlarga asoslangan hisob-kitob yoki qiymatni qaytaradigan ifoda. Bu ifoda birinchi qator bo'lishi 
kerak va unda hech qanday return kalit so'zi bo'lmaydi.
"""

x2 = lambda x: x * 2
print(x2(3))

numbers_sum = lambda x, y: x + y
print(numbers_sum(2, 3))

# sort list
words = ['banana', 'apple', 'orange', 'kiwi']
sorted_list = sorted(words, key=lambda x: len(x))
print(sorted_list)

# juft/toq
check_parity = lambda x: "juft" if x % 2 == 0 else 'toq'
print(check_parity(3))

# ax(2) + bx+c=0 -> kv tenglama ildizlarini topish uchun lambda example kod
import math

quadratic_roots = lambda a, b, c: (
    (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a),
    (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
) if b ** 2 - 4 * a * c >= 0 else "no real roots"

if __name__ == "__main__":
    print(quadratic_roots(1, -3, 2))  # (2.0, 1.0)
    print(quadratic_roots(1, 2, 5))
