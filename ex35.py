from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print "There is a bear here."
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."
            bear_moved = True

def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    next = raw_input("> ")
    
    if next == "left":
        bear_room()
    else:
        dead("You stumble around the room until you starve.")

start()
