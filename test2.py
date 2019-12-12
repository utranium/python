#Unpacking explicite avec une liste puis un dictionnaire.

def aire_rectangle(a, b):
	return a*b

def aire_rectangle(cote1=0, cote2=0):
	return cote1*cote2

if __name__ == '__main__':
	rec1 = [3,8]
	rec2 = {'cote1':4, 'cote2':8}
	#la liste rec1 va etre dépaquetée en arguments unitaire.
	print(aire_rectangle (*rec1))
	#le dictionnaire rec2 va etre dépaqueté en arguments unitaire
	print(aire_rectangle (**rec2))
