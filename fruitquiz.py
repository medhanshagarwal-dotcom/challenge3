import random
print("Welcome to fruitquiz")
class Fruitquiz:
    def __init__(self):
        self.fruits={'orange':'orange',
                     'apple':'red',
                     'mango':'yellow',
                     'watermelon':'green',
                     'dragonfruit':'pink'}
    def quiz(self):
        while True:
            fruit,color=random.choice(list(self.fruits.items()))
            print("What is the color of ", fruit)
            a=input()
            a.lower()
            if a==color:
                print("Correct answer")
            else:
                print("Wrong answer")
            
            o=int(input("Enter 0 to play again or 1 to stop: "))
            if o==1:
                break
f=Fruitquiz()
f.quiz()