
import sqlite3


def ulanish():
    """fanlar.db faylga ulanadi (fayl bo'lmasa o'zi yaratadi)"""
    return sqlite3.connect("fanlar.db")


def baza_yaratish():
    """fanlar jadvalini yaratadi (bir marta)"""
    con = ulanish()
    con.execute("""
        CREATE TABLE IF NOT EXISTS fanlar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fan_nomi TEXT,
            oqituvchi TEXT,
            soat INTEGER,
            xona TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    con.commit()
    con.close()
