import sqlite3


# Создание подключения и курсора
connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()
# Создание таблицы
cursor.execute("CREATE TABLE IF NOT EXISTS Users("
               "id INTEGER PRIMARY KEY,"
               "username TEXT NOT NULL,"
               "email TEXT NOT NULL,"
               "age INTEGER,"
               "balance INTEGER NOT NULL)")

# Заполнение БД
for i in range(1, 11):
   cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)",
                  (f"User{i}", f"example{i}@gmail.com", i * 10, 1000))

# Обновление данных в БД
for i in range(1, 11, 2):
    cursor.execute("UPDATE Users SET balance = 500 WHERE id = ?", (i, ))

# Удаление данных из БД
for i in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE id = ?", (i, ))

# Выбрать всех пользователей, где возраст не равен 60
cursor.execute("SELECT * FROM Users WHERE NOT age = 60")
users = cursor.fetchall()
for user in users:
    print(f"Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}")


# Сохранить данные, закрыть подключение
connection.commit()
connection.close()
