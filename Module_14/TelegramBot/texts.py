on_start_text = "Привет! Я бот помогающий твоему здоровью."
all_messages_text = "Введите команду /start, чтобы начать общение."
formulas_text = "для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5\n"\
                "для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161."
product_info_text = [
    "Название: Product1 | Описание: описание 1 | Цена: 100",
    "Название: Product2 | Описание: описание 2 | Цена: 200",
    "Название: Product3 | Описание: описание 3 | Цена: 300",
    "Название: Product4 | Описание: описание 4 | Цена: 400",
]
product_info_img = [
    "imgs/img1.png",
    "imgs/img2.png",
    "imgs/img3.jpg",
    "imgs/img4.png"
]
def formula_result(data):
    return f"Необходимое количество килокалорий в сутки для мужчин:"\
           f"{10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) + 5}\n"\
           f"Необходимое количество килокалорий в сутки для женщин:"\
           f"{10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) - 161}\n"