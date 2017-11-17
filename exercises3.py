# cd /Users/bkatchmar/GitHub/InflowPythonExercises
# python3 exercises3.py
import pets

def MakeThePetSoundOff(thepet):
    if (isinstance(thepet, pets.Pet)):
        print(thepet.SaySomething())
    else:
        print("Class is not an instance of pets.Pet")
        
mydog = pets.Dog("Brutus", 2)
mycat = pets.Cat("Floyd", 10)

MakeThePetSoundOff(mydog)
MakeThePetSoundOff(mycat)