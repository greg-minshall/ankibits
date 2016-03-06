# ONETAG: (anki menu item)

# want a function that, given an argument, will ensure that 1) the
# current deck has only cards with TAG; 2) all cards in Anki with TAG
# are in that deck.

# so, first, find all cards *not* in the current deck with TAG.  then,
# move all those cards from their previous deck to the current deck.

# XXX should we check we're not moving *too* many cards?

# then, search the current deck and find all cards that do *not* have
# the the designated tag.  delete all those cards.

# XXX same, should we check we're not deleting too many cards?

# remove the menu item (or, at least, the pre-canned tag)

# after all this, *delete* the tags from all cards in the current
# deck.

# ANKI-IMPORT: (shell command)
# usage: run the import operation, which cons up TAG, and adds it to
# all the cards in the deck, then imports the cards into the named
# deck: ./anki-import turkish-2015 turkish-2015.html after the import,
# prime a menu item in Anki (with a shortcut, hopefully), that will
# cause onetag to run with the correct tag.

