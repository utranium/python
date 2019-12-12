#packing explicite

def aire_rectangle(*args):
# Les arguments passés en parametre
#sont paquetés dans args qui se comporte comme un tuple
	if len(args) == 2:
		return args[0]*args[1]
	else:
		print('merci de stipuler deux parametres')

def aire_rectangle2(**kwargs):
# Les arguments passés en parametres
#sont paquetés dans kwarg qui se comporte comme un dictionnaire.
	if len(kwargs) == 2:
		result = 1
		for key, value in kwargs.items():
			result *=value
		return result
	else:
		print('merci de stipuler 2 parametres')

if __name__ == '__main__':
	#une liste va etre créee a partir des arguments fournis.
	print((aire_rectangle(3, 8)))
	#un dictionnaire va etre créé a partir des arguments fournis.
	print((aire_rectangle2(cote1=4, cote2=8)))
