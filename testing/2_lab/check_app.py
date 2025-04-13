from app import Figure

f1 = Figure("квадрат", 5)
print(f1.get_figure_type)   # має бути "квадрат"
print(f1.get_figure_length) # буде помилка — поверне тип замість довжини
