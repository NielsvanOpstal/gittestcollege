import random

Names = ['Stephen', 'Daan', 'Kees']

def get_name():
    naam = random.choice(Names)
    return naam

print("Hallo ik ben {naam}".format(naam=get_name()))
