# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
file = 'config_sw1.txt'
def get_int_vlan_map(config_filename):
	access_dict = {}
	trunk_dict = {}
	ports = [access_dict, trunk_dict]
	with open(config_filename) as f:
		intf = ''
		for line in f:
			if line.startswith('interface Fast'):
				intf = line.strip()[10:]
			elif line.startswith(' switchport access vlan'):
				ports[0][intf] = int(line.split()[3])
			elif line.startswith(' switchport trunk allowed vlan'):
				vlans = ([int(vl) for vl in line.split()[4].split(',')])
				ports[1][intf] = vlans
	return tuple(ports)

ports_tuple = get_int_vlan_map(file)

print(ports_tuple[0])
print(ports_tuple[1])
