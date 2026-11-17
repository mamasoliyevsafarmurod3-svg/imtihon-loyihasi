
from db import baza_yaratish
from funksiyalar import qoshish, korish, qidirish

baza_yaratish()

while True:
    print("\n===== MENU =====")
    print("1. Ma'lumot qo'shish")
    print("2. Ma'lumotlarni ko'rish")
    print("3. Ma'lumot qidirish")
    print("0. Chiqish")
    tanlov = input("Tanlang: ")

    if tanlov == "1":
        qoshish()
    elif tanlov == "2":
        korish()
    elif tanlov == "3":
        qidirish()
    elif tanlov == "0":
        print("Dastur tugadi. Xayr!")
        break
    else:
        print("Noto'g'ri tanlov!")
