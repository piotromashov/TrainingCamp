import sys
import math

# cant_museos = int(raw_input())
# while(cant_museos != -1):
# 	museum_prices = map(int, raw_input().split())

# 	visitas = 0
# 	acumulado = 0
# 	for price in museum_prices:
# 		acumulado += price
# 		if(acumulado % 100 == 0):
# 			visitas += 1
# 			acumulado = 0

# 	print(visitas)
# 	cant_museos = int(raw_input())
		
# bailes = int(raw_input())
# posibilidades = 0

# for cubiconianos in xrange(1, bailes+1):

# 	for cuadradonianos in xrange(1, cubiconianos+1):
# 		value = cubiconianos * cuadradonianos
# 		for nlogonianos in xrange(0, cuadradonianos+1):
# 			if(cubiconianos*cuadradonianos + cubiconianos*nlogonianos + cuadradonianos*nlogonianos) == bailes:
# 				print(str(cubiconianos) + " " + str(cuadradonianos) + " " + str(nlogonianos))
# 				posibilidades+=1

# print posibilidades


# bailes = int(raw_input())
# posibilidades = 0

# for cubiconianos in xrange(1, bailes+1):
# 	val = min(bailes/cubiconianos, cubiconianos)
# 	for cuadradonianos in xrange(1, val+1):
# 		nlogonianos = (bailes - cubiconianos * cuadradonianos) / (cubiconianos+cuadradonianos * 1.0)
# 		if(nlogonianos <= cuadradonianos and nlogonianos.is_integer() and nlogonianos>=0):
# 			posibilidades+=1

# print posibilidades

# cities, budget = map(int, raw_input().split())

# cities_data = []

# for city in xrange(0, cities):
# 	cities_data.append(map(int, raw_input().split()))

# rescued_cities = 0
# costs_to_save = []
# for zombies, soldiers, cost in cities_data:	
# 	if zombies > soldiers*10:
# 		excess_zombies = zombies-soldiers*10.0
# 		costs_to_save.append( cost*math.ceil(excess_zombies/10.0) )
# 	else:
# 		rescued_cities += 1

# costs_to_save.sort()

# while(costs_to_save and budget >= costs_to_save[0]):
# 	budget -= costs_to_save.pop()
# 	rescued_cities += 1

# print rescued_cities


# def max_prefix(a, b):
# 	equals = 0
# 	for index in xrange(0, min(len(a), len(b))):
# 		if(a[index] == b[index]):
# 			equals += 1
# 		else:
# 			return equals
# 	return equals

# players = raw_input()
# team_one_names = raw_input().split()
# team_two_names = raw_input().split()

# acum = 0
# prefix = 0
# for name in team_one_names:
# 	aux = ''
# 	for other_name in team_two_names:
# 		value = max_prefix(name, other_name)
# 		if(value > prefix):
# 			prefix = value
# 			aux = other_name

# 	if aux in team_two_names:
# 		team_two_names.remove(aux)
# 		acum += prefix
# 		print team_two_names

# print acum




