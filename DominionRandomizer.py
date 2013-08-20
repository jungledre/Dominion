#!/usr/bin/env python

import random

print 'Time to play Dominion'

unshuffled_list = (['Cellar', 'Chapel', 'Moat', 'Chancellor', 'Village', 'Woodcutter', 'Workshop', 'Bureaucrat', 'Feast', 'Gardens', 'Militia', 'Moneylender', 'Remodel', 'Smithy', 'Spy', 'Thief', 'Throne Room', 'Council Room', 'Festival', 'Laboratory', 'Library', 'Market', 'Mine', 'Witch', 'Adventurer'])

shuffled_list = []

int = 10

while int > 0:
	r = random.randint(0, len(unshuffled_list)-1)
	shuffled_list.append(unshuffled_list[r])
	del unshuffled_list[r]
	int -= 1
	shuffled_list.sort()

print shuffled_list
