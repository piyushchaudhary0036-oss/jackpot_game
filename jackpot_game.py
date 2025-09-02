import random
def spl():
    m=random.randrange(1,11)
    print("GUESS NUMBER AND GET A CHANCED TO WIN JACKPOT OF 7 LACKS")
    print()
    print('you have 5 chances to win the game')
    print('guess a number between 1 and 10')
    a=0
    while a<5:
        n=int(input('enter the number:'))
        if n==m:
            print('congratulations! you won the match & you win jackpot of 7lacs get rewards from the main counter')
            break
        else:
            if n<m:
                print('opps!your number is lower than the actual number')
            elif n>m:
                print('opps!your number is higher than the actual number')
            print('now u have ',4-int(a),'chances to guess')
            
        a=a+1
        if a==5:
            print('you lose the game Better luck next time')
            print(m,'is actual number')
spl()
while True:
    try:
        print('press ctrl+c to stop the game run')
        o=input('do u want to play again?(y/n)??')
        if o=='y' or o=='Y':
            print('game restart')
            spl()
        else:
            print('GAME OVER')
    except KeyboardInterrupt as k:
        break
    finally:
        print('game finished')
        print('have a good day')
        
        
