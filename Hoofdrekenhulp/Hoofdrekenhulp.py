import os
from Hoofdrekenfuncties import *

#begin van ons programma
os.system("clear")
print "Welkom bij Hoofdrekenhulp v0.1"

niveau = kies_niveau()

#De scores
aantal_sommen = 0
aantal_goed = 0
aantal_fout = 0
procent_goed = 100.00

#mainloop
while True:
	
	# 1 maak het sherm leeg en print de score
	os.system("clear")
	print "goed: %i - fout: %i - totaal: %i - %.2f%% goed" % (aantal_goed, aantal_fout, aantal_sommen, procent_goed)
	
	# 2 maak de som aan en tel 1 op bij het aantal sommen
	som = random_som(niveau)
	aantal_sommen = aantal_sommen + 1
	
	# 3 print de soms
	print_zonder_nieuwregel(som[0])
	
	# 4 geef antwoord
	antwoord = int_input()
	
	# 5 controleer antwoord
	if antwoord == som[1]:
		aantal_goed = aantal_goed + 1
	else:
		aantal_fout = aantal_fout + 1
	
	# 6 bereken het percentage goed
	procent_goed = 100 * float(aantal_goed)/float(aantal_sommen)




