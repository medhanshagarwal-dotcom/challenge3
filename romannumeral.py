import roman
class Rome:
    def num(x):
        x=int(input("Enter a number: "))
        print(roman.toRoman(x))
n=Rome()
while True:
    n.num()
    i=int(input("Enter 1 to exit and anyother number to continue: "))
    if i==1:
        break