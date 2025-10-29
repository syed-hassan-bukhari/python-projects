import random 

def mad_lib():

    noun = input("enter a noun: ")
    verb = input("enter a verb: ")
    adjective = input("enter an adjective: ")
    place = input("enter a place: ")
    animal = input("enter an animal: ")


    stories = [
        f"today i saw a {adjective} {animal} tryin to {verb} near the {place}.",
        f"once upon a time, there was a {adjective} {noun} that loved to {verb} at {place}.",
        f"one day, a {adjective} {animal} enterd the {place} and began to {verb} with a {noun}."

    ]

    story=random.choice(stories)
    print("\n YOUR MAD LIB STORY ")
    print(story)
     

mad_lib()
