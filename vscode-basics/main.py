import time

# Записуємо час на початку виконання
start_time = time.perf_counter()

for _ in range(100):
   
# Виконуємо якусь операцію
    for _ in range(1_000_000):
        pass  # Просто проходить цикл мільйон разів

# Записуємо час після виконання операції
end_time = time.perf_counter()

# Розраховуємо та виводимо час виконання
execution_time = end_time - start_time
print(f"Час виконання: {execution_time} секунд")
