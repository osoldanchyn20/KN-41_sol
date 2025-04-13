class Name:
    def __init__(self, name, hobby) -> None:
        if name not in ["Оля", "Анонім", "Олександра"]:
            raise ValueError("Дозволені імена: Оля, Анонім, Олександра")
        if not hobby:
            raise ValueError("Хоббі не може бути пустим!")
        self.name = name
        self.hobby = hobby

# Приклади
a = Name("Чарлі", "читання")
# b = Name("Анонім", "")
# c = Name("Олександра", "малювання")
