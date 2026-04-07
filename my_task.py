login_attempts = [
    "192.168.1.15", "10.0.0.5", "192.168.1.15", "192.168.1.100","192.168.1.100",
    "10.0.0.5", "192.168.1.15", "10.0.0.5", "192.168.1.15","192.168.1.100",
    "172.16.0.2", "192.168.1.100", "10.0.0.5"
]

def count_with_dict(attempts):
    ip_counts = {}  # Створюємо порожній словник (наш "журнал")

    # КРОК 1: Заповнюємо журнал (йдемо по списку лише один раз!)
    for ip in attempts:
        
        if ip in ip_counts:
            ip_counts[ip] += 1  # Якщо IP вже є в журналі, збільшуємо лічильник на 1
        else:
            ip_counts[ip] = 1   # Якщо бачимо IP вперше, записуємо його з цифрою 1

    # КРОК 2: Перевіряємо, у кого більше 3 спроб
    for ip, count in ip_counts.items(): # .items() дістає і IP, і його кількість
        if count > 3:
            print(f"Увага! IP {ip} здійснив {count} спроб!")

count_with_dict(login_attempts)
# def count_login_attempts(attempts):
#     for attempt in set(attempts):
#         if attempts.count(attempt) > 3:
#             print(f"Warning: Multiple login attempts from {attempt} detected!")


# count_login_attempts(login_attempts)