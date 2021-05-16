import itertools
print("Usage:   A*c*e*\n\n*\t=\tChar/'Num'/'Symbol'")
inp=input("Enter the sample word:")
Command=int(input("Replace * with ? \n\n1)UpperChar\n2)Lower Char\n3)Int\n4)Symbol\n5)All\n6)SSpecial\n7)Custom\n\nEnter Input : "))
n=inp.count("*")
min_length, max_length =n,n
out=inp
f=open("wordlist.txt","w")

def find_stars(seq=inp,item="*"):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

def get_chars(cmd):
    c = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = "0123456789"
    s = "!@#$%^&*_-.?"
    ss= "!@#$%^&*()-_.?]["
    if cmd==1:
        return c.upper()
    elif cmd==2:
        return c.lower()
    elif cmd==3:
        return n
    elif cmd==4:
        return s
    elif cmd==5:
        return c+c.lower()+n+s
    elif cmd==6:
        return ss
    else:
        return input("enter custom characters : ")



lst=[]

def gen_wordlist(chrs,o):
    for _ in range(min_length, max_length+1):
        for xs in itertools.product(chrs, repeat=_):
            lst.append(list(xs))
    
    for _ in lst:
        for nnn in range(len(_)):
            o = o[:loc[nnn]] + _[nnn] + o[loc[nnn]+1:]
        f.write(o+"\n")



loc     =   find_stars()
chrs    =   get_chars(Command)
size    =   (((len(chrs)**n)*len(inp))/(8))*10
print("Output Wordlist Size :",size//1048576,"MB\n do you want to continue[Y/N] : ")
start   =   input()
if (start.upper()=="Y"):
    gen_wordlist(chrs,out)
else:
    raise Exception("Operation aborted")
f.close()
print("finished")