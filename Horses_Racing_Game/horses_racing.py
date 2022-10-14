import random

from classes import HorsesRacing


def random_contender():
        contender={
        "name":['Kind','Alex', 'Lilly','Sugar','Lady','Cash','Lucky','Kind','Chance','Rose',],
        "Breed":["american", "arabian", "thoroughbred",'gypsy','andalusian'],
        "Point":[50,60,70,80,90,100]
        }
        return [random.choice(contender['name']),random.choice(contender['Breed']),random.choice(contender['Point'])]


if __name__ == "__main__":
    horse = HorsesRacing()
    horse.set_name(input("Enter your Horse name => "))
    # print(horse.get_name())
    horse.set_Breed(input('choose his Breed : \n ["american", "arabian", "thoroughbred","gypsy","andalusian"]\n => '))

    # print(horse.get_Breed())  

    contender = HorsesRacing()
    contender.set_name(random_contender()[0])
    # print(horse.get_name())
    contender.set_Breed(random_contender()[1])
    contender.set_point(random_contender()[2])
    from time import sleep
    sleep(2)
    print(horse)
    print(contender)
    horse.racing(contender)
    contender.set_name(random_contender()[0])
    # print(horse.get_name())
    contender.set_Breed(random_contender()[1])
    contender.set_point(random_contender()[2])
    print(horse)
    print(contender)
    horse.racing(contender)
    contender.set_name(random_contender()[0])
    # print(horse.get_name())
    contender.set_Breed(random_contender()[1])
    contender.set_point(random_contender()[2])
    print(horse)
    print(contender)
    horse.racing(contender)
    print(horse)
    print(contender)
    horse.racing(contender)
    print(horse)
    print(contender)
    horse.racing(contender)
    print(horse)
    print(contender)
    print(HorsesRacing.get_round_numbers())
