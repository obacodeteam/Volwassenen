import random, sys

def int_input():
	while True:
		getal = raw_input()
		try:
			getal = int(getal)
			return getal
		except:
			print "Je kunt alleen gehele getallen invoeren!"
		
def kies_niveau():
	niveau = 0
	while niveau != 1 and  niveau != 2 and niveau != 3:
		print "Kies een niveau: 1, 2 of 3:"
		niveau = int_input()
	return niveau

def random_som(niveau):
	getal1 = random.randrange(1,10**niveau+1)
	getal2 = random.randrange(1,10**niveau+1)
	
	soort_som = random.randrange(0,3)
	
	som_string = ""
	antwoord = 0
	
	if soort_som == 0:
		#optellen
		som_string = "%i + %i" % (getal1, getal2)
		antwoord = getal1 + getal2
	elif soort_som == 1:
		#aftrekken
		som_string = "%i - %i" % (getal1, getal2)
		antwoord = getal1 - getal2
	elif soort_som == 2:
		#vermenigvuldigen
		som_string = "%i * %i" % (getal1, getal2)
		antwoord = getal1 * getal2
	return [som_string, antwoord]

def print_zonder_nieuwregel(te_printen_content):
	sys.stdout.write(te_printen_content+" = ")
