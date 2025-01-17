### Ejercicio 1

# As you can see, he's hit a bit of bad luck recently. He wants to tweet this along with some choice emojis,
# but, as it looks right now, his followers will probably find it confusing. He's asked if you can help 
# him make the following changes:

# Add the title "Results of 500 slot machine pulls"
# Make the y-axis start at 0.
# Add the label "Balance" to the y-axis

def prettify_graph(graph):
    """Modify the given graph according to Jimmy's requests: add a title, make the y-axis
    start at 0, label the y-axis. (And, if you're feeling ambitious, format the tick marks
    as dollar amounts using the "$" symbol.)
    """
    graph.set_title("Results of 500 slot machine pulls")
    graph.set_ylabel("Balance")
    graph.set_ylim(0, 500)
    # print(dir(graph))
    # help(graph.yaxis.set)
    ticks = graph.get_yticks()    
    new_labels = ['${}'.format(int(amt)) for amt in ticks]
    graph.set_yticklabels(new_labels)
    
    

# graph = jimmy_slots.get_graph()
# prettify_graph(graph)
# graph


### Ejercicio 2

# This is a very challenging problem. Don't forget that you can receive a hint!

# Luigi is trying to perform an analysis to determine the best items for winning races 
# on the Mario Kart circuit. He has some data in the form of lists of dictionaries that look like...

# [
#     {'name': 'Peach', 'items': ['green shell', 'banana', 'green shell',], 'finish': 3},
#     {'name': 'Bowser', 'items': ['green shell',], 'finish': 1},
#     # Sometimes the racer's name wasn't recorded
#     {'name': None, 'items': ['mushroom',], 'finish': 2},
#     {'name': 'Toad', 'items': ['green shell', 'mushroom'], 'finish': 1},
# ]
# 'items' is a list of all the power-up items the racer picked up in that race, and 'finish' 
# was their placement in the race (1 for first place, 3 for third, etc.).

# He wrote the function below to take a list like this and return a dictionary mapping each item 
# to how many times it was picked up by first-place finishers.

# However, when he tried running it on his full dataset, the program crashed with a TypeError.

# Can you guess why? Try running the code cell below to see the error message Luigi is getting.
# Once you've identified the bug, fix it in the cell below (so that it runs without any errors).

# Import luigi's full dataset of race data
# from learntools.python.luigi_analysis import full_dataset
    
# Fix me!
def best_items(racers):
    winner_item_counts = {}
    for i in range(len(racers)):
        # The i'th racer dictionary
        racer = racers[i]
        iteration = i
        # We're only interested in racers who finished in first
        if racer['finish'] == 1:
            for i in racer['items']:
                # Add one to the count for this item (adding it to the dict if necessary)
                if i not in winner_item_counts:
                    winner_item_counts[i] = 0
                winner_item_counts[i] += 1

        # Data quality issues :/ Print a warning about racers with no name set. We'll take care of it later.
        if racer['name'] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
                iteration+1, len(racers), racer['name'])
                 )
    return winner_item_counts

# Try analyzing the imported full dataset
# best_items(full_dataset)


### Ejercicio 3

# Suppose we wanted to create a new type to represent hands in blackjack. One thing we might want to do
# with this type is overload the comparison operators like > and <= so that we could use them to check 
# whether one hand beats another. e.g. it'd be cool if we could do this:

# >>> hand1 = BlackjackHand(['K', 'A'])
# >>> hand2 = BlackjackHand(['7', '10', 'A'])
# >>> hand1 > hand2
# True
# Well, we're not going to do all that in this question (defining custom classes is a bit beyond the scope 
#                                                        of these lessons), but the code we're asking you
# to write in the function below is very similar to what we'd have to write if we were defining our own 
# BlackjackHand class. (We'd put it in the __gt__ magic method to define our custom behaviour for >.)

# Fill in the body of the blackjack_hand_greater_than function according to the docstring.

def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    def hand_total(hand):
        total = 0
        aces = 0
        
        for card in hand:
            if card in ['J', 'Q', 'K']:  # Cartas con valor 10
                total += 10
            elif card == 'A':  # Contamos ases por separado
                aces += 1
            else:  # Cartas numéricas
                total += int(card)

        # Ajustar el valor de los ases para no exceder 21
        for _ in range(aces):
            if total + 11 <= 21:
                total += 11
            else:
                total += 1

        return total

    total_1 = hand_total(hand_1)
    total_2 = hand_total(hand_2)

    if total_1 > 21:  
        return False
    if total_2 > 21:  
        return True
    return total_1 > total_2  

# Check your answer
# q3.check()