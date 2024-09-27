from time import sleep


class UrTube:                                       # Класс UrTube
    def __init__(self):                             # Конструктор класса
        self.users = list()                         # Создание списка пользователей
        self.videos = tuple()                       # Создание списка видео
        self.current_user = None                    # Текущий пользователь

    def log_in(self, nickname, password):           # Входа в UrTube
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user

    def register(self, nickname, password, age):    # Регистрация в UrTube
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        self.users.append(User(nickname, password, age))
        self.log_in(nickname, password)

    def log_out(self):                              # Выход из текущего аккаунта
        self.current_user = None

    def add(self, *videos):                         # Добавить видео в список видео
        self.videos += videos

    def get_videos(self, find):                     # Поиск видео по слову
        finded_videos = list()
        for video in self.videos:
            if video.title.lower().__contains__(find.lower()):
                finded_videos.append(video.title)
        return finded_videos

    def watch_video(self, video_name):              # Просмотр видео
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video == video_name:
                if video.adult_mode and self.current_user.age >= 18:
                    for current_second in range(video.duration):
                        video.time_now += 1
                        print(video.time_now, end=' ')
                        sleep(1)
                    print("Конец видео")
                else:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")


class Video:                                        # Класс видео
    def __init__(self, title, duration, time_now=0, adult_mode=False):  # Конструктор класса принимающий
        self.title = title                                              # заголовок, общее время видео,
        self.duration = duration                                        # текущее время, возрастное ограничение
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):                        # Метод __eq__ для удобного сравнения названий видео
        return self.title == other


class User:                                         # Класс ползователя
    def __init__(self, nickname, password, age):    # Конструктор класса, принимающий аргументы имя, пароль, возраст
        self.nickname = nickname
        self.password = hash(password)
        self.age = int(age)

    def __str__(self):                              # Метод __str__ для читабельности пользователя
        return self.nickname


# Исходные данные
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
