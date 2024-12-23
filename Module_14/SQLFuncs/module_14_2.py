import sqlite3

# Создание подключения и курсора
connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()
"""
    Удалить из базы данных not_telegram.db запись с id = 6.
    Подсчитать общее количество записей.
    Посчитать сумму всех балансов.
    Вывести в консоль средний баланс всех пользователей.
"""
# Удалить из базы данных not_telegram.db запись с id = 6.
cursor.execute("DELETE FROM Users WHERE id = 6")

# Подсчитать общее количество записей.
cursor.execute("SELECT COUNT(*) FROM Users")
users_quantity = cursor.fetchone()[0]
print(f"Количество пользователей: {users_quantity}")

# Посчитать сумму всех балансов.
cursor.execute("SELECT SUM(balance) FROM Users")
total_users_balance = cursor.fetchone()[0]
print(f"Сумма всех балансов пользователей: {total_users_balance}")

# Вывести в консоль средний баланс всех пользователей.
cursor.execute("SELECT AVG(balance) FROM Users")
print(f"Средний баланс всех пользователей (SQL-запрос): {cursor.fetchone()[0]}\n"
      f"Средний баланс всех пользователей (Python): {total_users_balance / users_quantity}")

# Закрыть подключение
connection.close()
