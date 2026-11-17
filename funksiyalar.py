
from db import ulanish


def qoshish():
    """Yangi fan kiritadi va jadvalga saqlaydi (INSERT)"""
    nom = input("Fan nomi: ")
    oqituvchi = input("O'qituvchi: ")
    soat = int(input("Haftalik soat: "))
    xona = input("Xona: ")

    con = ulanish()
    con.execute(
        "INSERT INTO fanlar (fan_nomi, oqituvchi, soat, xona) VALUES (?, ?, ?, ?)",
        (nom, oqituvchi, soat, xona),
    )
    con.commit()
    con.close()
    print("Saqlandi!")


def korish():
    """Barcha fanlarni ekranga chiqaradi (SELECT)"""
    con = ulanish()
    for qator in con.execute("SELECT id, fan_nomi, oqituvchi, soat, xona FROM fanlar"):
        print(qator)
    con.close()


def qidirish():
    """Fan nomi bo'yicha qidiradi (SELECT ... WHERE)"""
    nom = input("Qidiriladigan fan nomi: ")
    con = ulanish()
    natija = con.execute(
        "SELECT id, fan_nomi, oqituvchi, soat, xona FROM fanlar WHERE fan_nomi LIKE ?",
        ("%" + nom + "%",),
    ).fetchall()
    if natija:
        for qator in natija:
            print(qator)
    else:
        print("Topilmadi")
    con.close()
