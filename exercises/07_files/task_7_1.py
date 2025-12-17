# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

with open('ospf.txt') as f:
	for line in f:
		ospf = line.split()
		prefix = ospf[1]
		metric = ospf[2].replace(']', '').replace('[', '')
		nexthop = ospf[4].replace(',', '')
		l_update = ospf[5].replace(',', '')
		out_int = ospf[6]
		print(f"{'Prefix':20} {prefix:<25}")
		print(f"{'AD/Metric':20} {metric:<25}")
		print(f"{'Next-Hop':20} {nexthop:<25}")
		print(f"{'Last update':20} {l_update:<25}")
		print(f"{'Outbound Interface':20} {out_int:<25}")
