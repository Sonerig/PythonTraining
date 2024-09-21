def send_email(message, recipient, *, sender="university.help@gmail.com"):
    # Проверка на содержание символа '@' и на домен верхнего уровня
    if not (recipient.__contains__('@') and recipient.endswith((".com", ".ru", ".net"))
            and sender.__contains__('@') and sender.endswith((".com", ".ru", ".net"))):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    # Проверка на отправку самому себе
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    # Проверка на стандартного отправителя
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    # Вывод при нестандартном отправителе
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


# Пример выполняемого кода
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
