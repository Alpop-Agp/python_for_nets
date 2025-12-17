# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv
f_name = argv[1]
f_out_name = argv[2]
ignore = ["duplex", "alias", "configuration"]
with open(f_name) as f, open(f_out_name, 'w') as o:
	for line in f:
		bad_word = False
		for word in ignore:
			if word in line:
				bad_word = True
		if not line.startswith('!') and not bad_word:
			o.write(line) 

