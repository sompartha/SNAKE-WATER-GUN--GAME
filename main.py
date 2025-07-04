import random

'''
1 for Snake 
-1 for water
0 for gun
'''

Computer =random.choice((-1,0,1))
yourstr=input("Enter your choice ")
youDict={"s":1,"w":-1,"g":0}
reversedict={1:"Snake",-1:"Water",0:"Gun"}
you=youDict[yourstr]
print(f"You choose {reversedict[you]}\n  Computer chose {reversedict[Computer]}")

if(Computer==you):
    print("Its a draw")
else:
    if(Computer ==-1 and you == 1):
        print("You win")
    elif(Computer==-1 and you==0):
        print("You loose ")
    elif(Computer== 1 and you==-1):
        print("You loose ")
    elif(Computer== 1 and you==0):
        print("You win ")
    
    elif(Computer==0 and you==-1):
        print("You win ")
    elif(Computer==0 and you==1):
        print("You loose ")
    
    else:
        print("Something went wrong")
