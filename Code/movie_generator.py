from random import randrange

i=0
movie=[]

while(True):
    x=input("Enter the movie to exit enter 0: ")
    if(x=="0"):
        break
    else:
        movie.append(x)
        i+=1

if(i!=0):
    ran=randrange(i-1)
    print("\nWatch",movie[ran],"today!!");

n=input("\nPress Enter to exit....To run again enter 1")

if(n=="1"):
    os.system("cls")
    os.execv(sys.argv[0], sys.argv)
