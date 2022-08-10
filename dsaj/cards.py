# cards[]: list containing cards
# query: the number to search
# position: index

def locate_cards(cards, query):
    position = 0
    #print('cards:', cards)
    #print('query:', query)

    #the position has to be less than the len(cards) so we can access it.
    while position < len(cards):
        #print('position:', position)
        cards.sort()
        if cards[position] == query:
            
            print('cards:', cards)
            return position
        position += 1
    return -1

a = [9, 8, 7, 5, 4, 2, 1]
b = 7

c = locate_cards(a, b)
print(c)