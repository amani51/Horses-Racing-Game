import sys
import random
import time
from classes import HorsesRacing


def random_contender():
    contender={
    "name":['Kind','Alex', 'Lilly','Sugar','Lady','Cash','Lucky','Kind','Chance','Rose',],
    "Breed":["american", "arabian", "thoroughbred",'gypsy','andalusian'],
    "Point":[50,60,70,80,90,100]
    }
    return [random.choice(contender['name']),random.choice(contender['Breed']),random.choice(contender['Point'])]

def draw_horse():
    a="""
    ******************************************
    welcome to             O  ,--.
    Horse Racing Game   _ /|\/  /\|
                    ,;( )__7,  )
                    /  //  // '--.
                    '    \,   ,' '
    *******************************************
    """

    print(a, end="\r")
#     sys.stdout.write('\r'+b)
    time.sleep(.5)
       


if __name__ == "__main__":
    draw_horse()
    horse = HorsesRacing()
    print(str(horse))
    horse.set_name("Rose")
 
    horse.set_Breed("thoroughbred")
    contender = HorsesRacing()
    contender.set_name("king")
    contender.set_Breed("arabian")
    contender.set_point(70)
    print(contender)
    print(horse.get_point())
    print(contender.get_point())

    print(HorsesRacing.get_round_numbers())
