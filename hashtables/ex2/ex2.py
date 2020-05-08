#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    d = {}

    route = []

    nxt_location = "NONE"

    for t in tickets:   
        if t.source not in d:
            d[t.source] = t.destination

    while len(route) < length:

        for ticket in d:
            if ticket == nxt_location and d[ticket] not in route:
                route.append(d[ticket])
                nxt_location = d[ticket]
            else:
                continue

    return route
