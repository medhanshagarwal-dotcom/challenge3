class Flashcard:
    def __init__(self, w, m):
        self.m=m
        self.w=w
    
    def __str__(self):
        
        return self.w + '(' + self.m + ")"

flash=[]

print("Lets create a flash card")
while True:
    m=input("Enter a word for the flashcard: ")
    w=input("Enter the meaning of the word: ")
    flash.append(Flashcard(w ,m))
    o=int(input("Enter 0 for one more flash card or 1 to stop: "))

    if o==1:
        break

for i in flash:
    print( ">", i)