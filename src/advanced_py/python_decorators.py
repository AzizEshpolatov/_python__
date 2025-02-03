"""
Decoratorlar - bu method yoki class-larni orab ularning hatti harakatini ozgartirish yoki kengaytirish imkonini
beruvchi obyektlardir. Dekoratorlar asosan kodni qayta ishlash imkoniyatini oshiradi, va ortiqcha yoziladigan
kodlarni minimallashtirishda yordamlashadi.
bu tushunchani funksiya uchun funksiya deb tushunchask ham boladi. Katta projectlarda kodni strukturalashni
soddalashtiradi.

Dekoratorlarni "@" belgisidan foydalanib qo'llash mumkin.
"""


# oddiy dekaratorsz method
def hello_func():
    print("Hi!!!")


hello_func()


# dekarator aralashgan method

def decorator(func):
    def wrapper_func():
        print("Funktsiya chaqirilishidan oldin")
        func()
        print("Funktsiya chaqirilishidan keyin")

    return wrapper_func


@decorator
def hello_function():
    print("hello")


hello_function()

# mavjud methodning bajarilish vaqtini hisoblaymiz!!
import time


def time_it(func):
    """funksiya bajarilish vaqtini aniqlaydigan decorator"""

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} funksiyasi {end_time - start_time:.7f} soniyada bajarildi")
        return result

    return wrapper


@time_it
def heavy_computation(n):
    """Og‘ir hisob-kitob funksiyasi"""
    total = 0
    for i in range(n):
        total += i ** 2
    return total


print(heavy_computation(10 ** 5))


# auth logic for user
def require_login(func):
    def wrapper_func(*args, **kwargs):
        user = kwargs.get("user")

        if not user or not user.get("is_authenticated", False):
            print("foydalanuvchi topilmadi!")
            return None

        return func(*args, **kwargs)

    return wrapper_func


@require_login
def get_user_data(*args, **kwargs):
    """Foydalanuvchi ma’lumotlarini olish"""
    user = kwargs.get('user')
    return f"Foydalanuvchi : {user['username']}"


print(get_user_data(user={"username": "Ali", "is_authenticated": True}))
print(get_user_data(user={"username": "Ali", "is_authenticated": False}))
