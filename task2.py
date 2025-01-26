
from decimal import Decimal


def sum_profit(text, func):
    # визначення та повернення суми згенерованих чисел
    return sum([Decimal(number).quantize(Decimal("0.00"))for number in func(text)]) 

def generator_numbers(text):
    for word in text.split():
        # ітерація по кожному слову тексту і перевірка чи це число
        if word[0].isnumeric():
            yield word

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
