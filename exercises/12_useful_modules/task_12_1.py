# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess
from pprint import pprint
ip_addresses = [
    "192.168.1.1",
    "192.168.1.2",
    "192.168.0.2",
    "8.8.8.8",
    "118.11.1.254",
]
def ping_ip_addresses(ip_addresses):
	ip_available = []
	ip_unavailable = []
	for ip in ip_addresses:
		reply = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.DEVNULL)
		if reply.returncode == 0:
			ip_available.append(ip)
		else:
			ip_unavailable.append(ip)
	return tuple([ip_available, ip_unavailable])

if __name__ == "__main__":
	pprint(ping_ip_addresses(ip_addresses))
