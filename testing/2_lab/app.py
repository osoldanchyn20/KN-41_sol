class Figure:
    FIGURES = ["квадрат", "прямокутник", "трикутник"]

    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length

    @property
    def get_figure_type(self):
        return self.type

    @property
    def get_figure_length(self):
        return self.type  # ПОМИЛКА! МАЄ БУТИ self.length

    @property
    def get_angles(self):
        if self.type in ["квадрат", "прямокутник"]:
            return 4
        if self.type == "трикутник":
            return 3



def test_app_triangle():
    """Тест якщо створено трикутник."""
    fig = "трикутник"
    triangle = Figure(fig, 4)
    assert triangle.type == fig, f"Фігура має бути {fig}"


if __name__ == '__main__':
    import unittest
    unittest.main()

def test_get_angles():
    """Тестуємо чи правильно повертається кількість кутів фігури."""
    fig = "трикутник"
    triangle = Figure(fig, 1)
    assert triangle.get_angles == 3, f"У {fig} є 3 кути!"
