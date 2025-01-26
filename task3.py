from collections import Counter
import sys

def parse_log_line(line: str) -> dict:
    # створюємо словник
    data = dict()
    sep_line = line.split(" ")
    data["date"] = sep_line[0]
    data["time"] = sep_line[1]
    data["command"] = sep_line[2]
    # інформацію зберігаємо як одне речення
    data["info"] = line.split(sep_line[2])[1].strip()
    return data

def load_logs(file_path: str) -> list:
    # для завантаження логів з файлу.
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        return "Не вдалося знайти файл."
    

def filter_logs_by_level(logs: list, level: str) -> list:
    # використання фільтра
    new_logs = filter(lambda log: log['command'].lower() == level.lower(), logs)
    return new_logs

def count_logs_by_level(logs: list) -> dict:
    return Counter(log['command'] for log in logs)

def display_log_counts(counts: dict):
    print("""Рівень логування | Кількість\n-----------------|----------""")
    for key in counts:
        print(f"{key+" "*(10-len(key))}       | {counts[key]}")

def main():
    lines = load_logs(sys.argv[1])
    logs = []
    for line in lines:
        # перевіряємо чи в лінії міститься команда ["DEBUG","INFO","ERROR","WARNING"]
        if len(line.split())>4 and line.split()[2].upper() in ["DEBUG","INFO","ERROR","WARNING"]:    
            logs.append(parse_log_line(line))
    display_log_counts(count_logs_by_level(logs))
    try:
        # перевірка чи користувач ввів коректну інформацію
        details = filter_logs_by_level(logs, sys.argv[2])
        if details:
            print(f"\nДеталі логів для рівня '{sys.argv[2].upper()}':")
            for line in details:
                print(" ".join(line.values()))
    except IndexError:
        pass
if __name__ == "__main__":
    main()
