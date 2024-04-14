import csv
import random
from datetime import datetime, timedelta

# Функция для генерации случайного IP-адреса


def generate_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

# Функция для генерации случайной даты и времени


def generate_timestamp(start_date, end_date):
    time_delta = end_date - start_date
    random_seconds = random.randint(0, round(time_delta.total_seconds()))
    random_time = start_date + timedelta(seconds=random_seconds)
    return random_time.strftime("%Y-%m-%d %H:%M:%S")

# Функция для генерации случайного порта


def generate_port():
    return random.randint(1, 65535)

# Функция для генерации случайного размера пакета


def generate_packet_length():
    return random.randint(50, 1500)

# Функция для генерации случайных флагов TCP


def generate_flags():
    flags = ['S', 'A', 'F', 'R', 'P', 'U']
    return "".join(random.choices(flags, k=3))


# Открываем файл для записи данных
with open('network_traffic.csv', 'w', newline='') as csvfile:
    fieldnames = ['timestamp', 'source_ip', 'destination_ip', 'protocol',
                  'source_port', 'destination_port', 'packet_length', 'flags', 'threat']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Задаем временной интервал для генерации данных
    start_date = datetime(2024, 4, 13, 0, 0, 0)
    end_date = datetime(2024, 4, 14, 0, 0, 0)

    # Генерируем 100000 пакетов
    for i in range(100000):
        timestamp = generate_timestamp(start_date, end_date)
        source_ip = generate_ip()
        destination_ip = generate_ip()
        protocol = random.choice(['TCP', 'UDP'])
        source_port = generate_port()
        destination_port = generate_port()
        packet_length = generate_packet_length()
        flags = generate_flags()

        # Добавляем случайную угрозу каждый 50-ый пакет
        threat = 'Normal' if (i + 1) % 50 != 0 else random.choice(['DDoS', 'DNS_Amplification', 'DNS_Poisoning',
                                                                   'Malware', 'Phishing'])

        writer.writerow({'timestamp': timestamp, 'source_ip': source_ip, 'destination_ip': destination_ip, 'protocol': protocol,
                         'source_port': source_port, 'destination_port': destination_port, 'packet_length': packet_length,
                         'flags': flags, 'threat': threat})
