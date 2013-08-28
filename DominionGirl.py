#!/usr/bin/env python

import random

def give10(deck):
	unshuffled_list = []

	i = 10

	if deck == "dominion":
		unshuffled_list = (['Cellar', 'Chapel', 'Moat', 'Chancellor', 'Village', 'Woodcutter', 'Workshop', 'Bureaucrat', 'Feast', 'Gardens', 'Militia', 'Moneylender', 'Remodel', 'Smithy', 'Spy', 'Thief', 'Throne Room', 'Council Room', 'Festival', 'Laboratory', 'Library', 'Market', 'Mine', 'Witch', 'Adventurer'])

	elif deck == "intrigue":
		unshuffled_list = (['Courtyard','Pawn','Secret', 'Chamber','Great Hall','Masquerade','Shanty Town','Steward','Swindler','Wishing Well','Baron','Bridge','Conspirator','Coppersmith','Ironworks','Mining Village','Scout','Duke','Minion','Saboteur','Torturer','Trading Post','Tribute','Upgrade','Harem','Nobles'])

		#elif deck == "seaside":
	else: # hopefully 'seaside', also default
		unshuffled_list = (['Embargo','Haven','Lighthouse','Native Village','Pearl Diver','Ambassador','Fishing Village','Lookout','Smugglers','Warehouse','Caravan','Cutpurse','Island','Navigator','Pirate Ship','Salvager','Sea Hag','Treasure Map','Bazaar','Explorer','Ghost Ship','Merchant Ship','Outpost','Tactician','Treasury','Wharf'])


	shuffled_list = []
	while i > 0:
		r = random.randint(0, len(unshuffled_list)-1)
		shuffled_list.append(unshuffled_list[r])
		del unshuffled_list[r]
		i -= 1
		shuffled_list.sort()

	return shuffled_list

if __name__ == "__main__":

	print '\n' + 'Time to play Dominion' + '\n' + '\n' + 'Which expansion would you like to use?' + '\n' + "	Dominion" + '\n' + "	Intrigue" + '\n' + "	Seaside" + '\n'

	while True:
		deck = raw_input()
		deck = deck.lower()

		if deck == 'dominion':
			break

		elif deck == 'intrigue':
			break

		elif deck == 'seaside':
			break

		else:
			print "Try that again." + '\n'




	print give10(deck)
