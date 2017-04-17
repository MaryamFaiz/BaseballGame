" Name: Maryam Faiz"
" This fuction calculates the number of pitches of Baseball game."

" The fuction accept a list as its parameter and return a value."
" It is an easy way to calculate the number of ball trown by taking the lenght of the list."
"Whereas datalist is the raws of the file."

DEBUG = True

def pitches (datalist):

 

    return len(datalist)



# This function calculates the number of hits in a Baseball game.

# The function accepts the list of hits and count the number of hits(1).
# The function has a return value.



def hit(hits):
       

       counthits = 0


       counthits = hits.count(1)

       return counthits



" This fucntion calculates the number of strike in a Baseball game by accepting the list of hits as it"

"parameter and return a value. the function counts the number of (0) in a hit list."


def strikes(hits):


       countstrikes = 0

       countstrikes = hits.count(0)
    
       return countstrikes 


# This function accepts a value as a list(hits list) and by using the count function of list it calculates the

# number of fouls in a Baeball game by counting the number of (-1) in a hitlist.
# the fucntion has a return value.

def fouls(hits):

    countfoul = 0

    countfoul = hits.count(-1)

    return countfoul

def avghitlength(length):

    c = 0
    a = 0

    for line in length:

        if(line > 0 ):

            c += 1

    a = sum(length) / c

    return round(a, 5)


def max_length_of_hits(length):



    return max(length)

# Calculate minimum, maximum and median of the length.
def min_length_of_hits(length):

    newlist = list()

    newlist = [x for x in length if x > 0]


    return min(newlist)

def median(length):

    length = [x for x in length if x >0]

    length = sorted(length)

    lenlist = len(length)
    index = (lenlist - 1) /2.0

    oddindex = int(index) + 1

   #print(length)

    if(lenlist % 2):


        return length[int(index)]
    else:

        return (length[int(index)] + length[oddindex]) / 2.0

    

def main():

    print("Greetings!")
    print("\nThe program is coded by Maryam Faiz")
    print("The program calculates number of:\nHits \nFoul \nStrikes")
    print("Also it calculates: \nAverage, Maximum,Minimum and Median of Length in a Basball Game")
    

    debug1 = True         
    hits = list()
    length = list()
    caught = list()
    datalist = list()
    s= -1
    pitch =0
    hitscount = -1
    
    while(debug1):


        try:

         filename = input ("\nEnter the file name as ""Filename.txt"":")

         filename = open(filename, "r")

         debug1 = False

         
         
        except FileNotFoundError:

            print("Please make sure you have entered a valid file name with .txt extenssion!!")
            

       # filename = open (filename, "r")



 
    for line in filename:
        
       # print("This is the line I just read in: " , line)
        s = line.split(" ")
        #print(s)

        hits.append(s[0])
        length.append(s[1])
        caught.append(s[2].strip("\n"))
        datalist.append(s)
        
    #print(datalist)
       
        
 #   pitch = pitches(datalist)

    if DEBUG: print(" Lists created")
        
        
    hits =   [float(h)  for h in hits]
    length = [int(l) for l in length]
    caught = [int(c) for c in caught]
    

    pitch = pitches(datalist)

    hitscount = hit(hits)
    countstrikes = strikes(hits)
    countfoul = fouls(hits)
    avghitslength = avghitlength(length)
    maxlengthofhits = max_length_of_hits(length)
    minlengthofhits = min_length_of_hits(length)
    medianofhits = median(length)

    print("\nThe Baseball has:")


    print("+ ---------------------------+")
    
    print("|Pitches", " \t| ", pitch, "      |")

    print("+ ---------------------------+")

    print("|Strikes ", "\t|",countstrikes,"        |")

    print("+----------------------------+")

    print("|Hits       ","\t|", hitscount, "        |")

    print("+----------------------------+")

    print("|Fouls "               , "\t|",countfoul,"        |")

    print("+----------------------------+")
    print("|Avarage Length","|",avghitslength,"  |")

    print("+----------------------------+")
    print("|Maximum Length", "|", maxlengthofhits,"       |")

    print("+----------------------------+")
    print("|Minimum Length", "|",minlengthofhits,"         |")

    print("+----------------------------+")
    print("|Median Length ", "|",medianofhits,"        |")

    print("+----------------------------+")
             

    #print(hits)
   # print(length)
    #print(cautgh)


 



main()

        
