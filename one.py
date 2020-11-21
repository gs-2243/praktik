import sqlite3 as sq

with sq.connect('Коммуналка.db') as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS жильцы  (
    id INTEGER,
    ФИО TEXT,
    Адрес INTEGER,
    долги INTEGER
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS платежи (
    Фио жильца TEXT,
    Сумма оплаты INTEGER,
    Дата платежа INTEGER,
    признак удаления TEXT
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS оплаченные (
    id INTEGER,
    ФИО жильца TEXT,
    дата оплаты INTEGER,
    сумма оплаты INTEGER,
    признак удаления TEXT
    )""")
    cur.execute("INSERT INTO жильцы(id, ФИО, Адрес, долги)VALUES(1, Абрамов 25 0)")

