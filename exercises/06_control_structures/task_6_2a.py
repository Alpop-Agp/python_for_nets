# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

result = True
okt1 = ''
okt2 = ''
okt3 = ''
okt4 = ''
ip = input("Enter ip address in format: ")
okts = ip.split('.')
if len(okts) == 4:
	okt1 = okts[0]
	okt2 = okts[1]
	okt3 = okts[2]
	okt4 = okts[3]
else:
	result = False
	
if not okt1.isdigit() or int(okt1) <  0  or int(okt1) > 255:
	result = False
if not okt2.isdigit() or int(okt2) <  0  or int(okt2) > 255:
	result = False
if not okt3.isdigit() or int(okt3) <  0  or int(okt3) > 255:
	result = False
if not okt4.isdigit() or int(okt4) <  0  or int(okt4) > 255:
	result = False

if not result:
    print('Неправильный IP-адрес')
elif int(okt1) > 0 and int(okt1) < 223:
	print('unicast')
elif int(okt1) > 223 and int(okt1) < 240:
	print('multicast')
elif ip == "255.255.255.255":
	print('local broadcast')
elif ip == "0.0.0.0":
	print('unassigned')
else:
	print('unused')
