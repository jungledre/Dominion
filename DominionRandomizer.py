#!/usr/bin/env python

import random

shuffled_list = []
unshuffled_list = []

print '\n' + 'Time to play Dominion' + '\n' + '\n' + 'Which expansion would you like to use?' + '\n' + "	Dominion" + '\n' + "	Intrigue" + '\n' + "	Seaside" + '\n'

while True:
	deck = raw_input()

	if deck == 'Dominion':
		break

	elif deck == 'Intrigue':
		break

	elif deck == 'Seaside':
		break

	else:
		print "Try that again." + '\n'

if deck == "Dominion":
	unshuffled_list = (['Cellar', 'Chapel', 'Moat', 'Chancellor', 'Village', 'Woodcutter', 'Workshop', 'Bureaucrat', 'Feast', 'Gardens', 'Militia', 'Moneylender', 'Remodel', 'Smithy', 'Spy', 'Thief', 'Throne Room', 'Council Room', 'Festival', 'Laboratory', 'Library', 'Market', 'Mine', 'Witch', 'Adventurer'])

elif deck == "Intrigue":
	unshuffled_list = (['Courtyard','Pawn','Secret', 'Chamber','Great Hall','Masquerade','Shanty Town','Steward','Swindler','Wishing Well','Baron','Bridge','Conspirator','Coppersmith','Ironworks','Mining Village','Scout','Duke','Minion','Saboteur','Torturer','Trading Post','Tribute','Upgrade','Harem','Nobles'])

elif deck == "Seaside":
	unshuffled_list = (['Embargo','Haven','Lighthouse','Native Village','Pearl Diver','Ambassador','Fishing Village','Lookout','Smugglers','Warehouse','Caravan','Cutpurse','Island','Navigator','Pirate Ship','Salvager','Sea Hag','Treasure Map','Bazaar','Explorer','Ghost Ship','Merchant Ship','Outpost','Tactician','Treasury','Wharf'])

int = 10

while int > 0:
	r = random.randint(0, len(unshuffled_list)-1)
	shuffled_list.append(unshuffled_list[r])
	del unshuffled_list[r]
	int -= 1
	shuffled_list.sort()

print shuffled_list
