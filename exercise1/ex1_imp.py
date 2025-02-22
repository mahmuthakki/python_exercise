import random

def guessing_challange():
    number = random.randint(1,100) # the generated number
    random_guesser= random.randint(1,100) # first guess of guesser 1
    guesser_with_method= 50 #first guess of guesser 2 
    top = 100
    bottom = 0
    while ((guesser_with_method!=number) and (random_guesser!=number)):
        random_guesser = random.randint(1,100)
        if number<guesser_with_method:
            top = guesser_with_method-1
        else:
            bottom = guesser_with_method+1
        guesser_with_method = (top+bottom)//2
    if guesser_with_method ==number:
        return 2
    else:
        return 1    
guesser_dict = {"guesser 1 ":0, "guesser 2":0}
for i in range(100000):
    a = guessing_challange()
    if a ==1:
        guesser_dict["guesser 1 "]+=1
    else:
        guesser_dict["guesser 2"]+=1 
print("The score for guesser 1 is {} and the score for guesser 2 is {}".format(guesser_dict["guesser 1 "],guesser_dict["guesser 2"]))           

                

