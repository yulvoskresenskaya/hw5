from datetime import datetime

formats = [
    '%A, %B %d, %Y',  # The Moscow Times
    '%A, %d.%m.%y',  # The Guardian
    '%A, %d %B %Y'  # Daily News
]

print("Введите даты в форматах газет:")
print("1. Wednesday, October 2, 2002 (The Moscow Times)")
print("2. Friday, 11.10.13 (The Guardian)")
print("3. Thursday, 18 August 1977 (Daily News)")
print("Для выхода введите 'q'")

while True:
    user_input = input("Введите дату: ").strip()

    if user_input.lower() == 'q':
        print("Выход")
        break

    date_parsed = None
    for fmt in formats:
        try:
            date_parsed = datetime.strptime(user_input, fmt)
            break
        except ValueError:
            continue

    if date_parsed:
        print(date_parsed)
    else:
        print("Неверный формат. Продолжаем...")