# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
file = 'config_sw2.txt'
def get_int_vlan_map(config_filename):
	access_dict = {}
	trunk_dict = {}
	ports = [access_dict, trunk_dict]
	with open(config_filename) as f:
		intf = ''
		for line in f:
			if line.startswith('interface Fast'):
				intf = line.strip()[10:]
				ports[0][intf] = 1
			elif line.startswith(' switchport access vlan'):
				ports[0][intf] = int(line.split()[3])
			elif line.startswith(' switchport trunk allowed vlan'):
				vlans = ([int(vl) for vl in line.split()[4].split(',')])
				ports[1][intf] = vlans
				del ports[0][intf]
	return tuple(ports)

ports_tuple = get_int_vlan_map(file)

print(ports_tuple[0])
print(ports_tuple[1])
