"""Binary search algorithms."""
# cards[]: list containing cards
# query: the number to search
# position: index

#1. find the middle element of the list
#2. if it matches queried number, return the middle position as the answer.
#3. if it is less than the queried number, then search the first half.
#4. if it is greater than the queried number, then search the second half.
#5. if no more elements remain, return -1.


def test_location(cards, query, middle):
    if cards[middle] == query:
        if middle - 1 >= 0 and cards[middle - 1] == query:
            return 'left'
        else:
            return 'found'
    elif cards[middle] < query:
        return 'left'
    else:
        return 'right'

def locate_cards(cards, query):
    start, end = 0, len(cards) - 1

    while start <= end:
        middle = (start + end) // 2
        result = test_location(cards, query, middle)
        if result == 'found':
            return middle
        elif result == 'left':
            end = middle - 1
        elif result == 'right':
            start = middle + 1
    return -1

a = [9, 8, 7, 5, 4, 2, 1]
b = 7

c = locate_cards(a, b)
print(c)
